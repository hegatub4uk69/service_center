<template>
  <v-card class="fill-height">
    <v-container class="fill-height" fluid="">
      <v-row align="center" justify="center" dense="">
        <v-col cols="12" sm="8" md="4" lg="4">
          <v-form
            v-model="form"
            @submit.prevent="onSubmit"
          >
            <v-card-text>
              <v-text-field
                v-model="username"
                :readonly="loading"
                :rules="[required]"
                clearable="true"
                label="Username"
                color="primary"
                prepend-inner-icon="mdi-account-circle-outline"
                hint="Введите логин для доступа к сайту"
              />
              <v-text-field
                v-model="password"
                :readonly="loading"
                :rules="[required]"
                :type="showPassword ? 'text' : 'Password'"
                clearable="true"
                label="Password"
                color="primary"
                prepend-inner-icon="mdi-lock-outline"
                hint="Введите пароль для доступа к сайту"
                :append-inner-icon="showPassword ? 'mdi-eye-outline' : 'mdi-eye-off-outline' "
                @click:append-inner="showPassword = !showPassword"
              />
            </v-card-text>
            <v-card-actions>
              <v-btn
                v-model="authorize"
                :disabled="!form"
                :loading="loading"
                type="submit"
                variant="elevated"
                color="success"
                size="large"
                class="ma-2"
                @click="login"
              >{{log_btn_name}}
              </v-btn>
            </v-card-actions>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import router from "@/router";

export default {
  name: 'LoginPage',
  data: () => ({
    showPassword: false,
    form: false,
    username: null,
    password: null,
    incorrectAuth: false,
    loading: false,
    authorize: false,
    log_btn_name: 'Авторизация',
  }),

  methods: {
    login() {
      this.$store.dispatch('userLogin', {
        username: this.username,
        password: this.password
      })
        .then(() => {
          router.push({name: 'profile'})
        })
        .catch(err => {
          console.log(err)
          this.incorrectAuth = true
        })
    },
    onSubmit() {
      if (!this.form) return
      this.loading = true
      setTimeout(() => (this.loading = false), 2000)
    },
    required(value) {
      return !!value || 'Поле обязательно для заполнения'
    },
  },
}
</script>
