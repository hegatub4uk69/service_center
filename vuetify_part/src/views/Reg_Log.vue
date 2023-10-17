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
                v-model="login"
                :readonly="loading"
                :rules="[required]"
                clearable="true"
                label="Username"
                color="primary"
                prepend-inner-icon="mdi-account-circle-outline"
                hint="Enter your login to access to website"
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
                hint="Enter your password to access to website"
                :append-inner-icon="showPassword ? 'mdi-eye-outline' : 'mdi-eye-off-outline' "
                @click:append-inner="showPassword = !showPassword"
              />
            </v-card-text>
            <v-card-actions>
              <v-btn
                v-model="register"
                :disabled="!form"
                :loading="loading"
                type="submit"
                variant="elevated"
                color="info"
                size="large"
                class="ma-2"
              >{{reg_btn_name}}
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn
                v-model="authorize"
                :disabled="!form"
                :loading="loading"
                type="submit"
                variant="elevated"
                color="success"
                size="large"
                class="ma-2"
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
export default {
  name: 'Reg_Log',
  data: () => ({
    showPassword: false,
    form: false,
    login: null,
    password: null,
    loading: false,
    authorize: false,
    register: false,
    log_btn_name: 'Авторизация',
    reg_btn_name: 'Регистрация',
  }),

  methods: {
    onSubmit() {
      if (!this.form) return
      this.loading = true
      setTimeout(() => (this.loading = false), 2000)
    },
    required(value) {
      return !!value || 'Field is required'
    },
  },
}
</script>
