<template>
  <v-card class="fill-height">
    <v-container>
      <v-row align="center" justify="center" dense="">
        <v-col cols="12" sm="8" md="4" lg="6">
          <v-row align="center" justify="center" dense="">
            <v-avatar image="/kompyuternyj-servis.png" size="300px"/>
          </v-row>
          <v-row align="center" justify="center" dense="" class="justify-center pb-5">
            <span class="title text-secondary py-2 font-weight-bold">{{ name }}</span>
          </v-row>
          <v-text-field
            :rules="[required]"
            label="Фамилия"
            prepend-inner-icon="mdi-card-account-details-outline"
          ></v-text-field>
          <v-text-field
            :rules="[required]"
            label="Имя"
            prepend-inner-icon="mdi-card-account-details-outline"
          ></v-text-field>
          <v-text-field
            label="Отчество (не обязательно)"
            prepend-inner-icon="mdi-card-account-details-outline"
          ></v-text-field>
          <v-text-field
            :rules="[required]"
            label="Логин"
            prepend-inner-icon="mdi-alpha-l-box-outline"
          ></v-text-field>
          <v-text-field
            label="Электронная почта (не обязательно)"
            prepend-inner-icon="mdi-email-outline"
          ></v-text-field>
          <v-text-field
            :rules="[required]"
            label="Номер телефона"
            prepend-inner-icon="mdi-phone-outline"
          ></v-text-field>
          <v-row align="center" justify="center">
            <v-col cols="12" md="6">
              <v-btn
                color="info"
                class="pa-6 font-weight-bold"
                block=""
                tile
                elevation="0"
              >Изменить
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'ProfilePage',
  methods: {
    onSubmit() {
      if (!this.form) return
      this.loading = true
      setTimeout(() => (this.loading = false), 2000)
    },
    required(value) {
      return !!value || 'Поле обязательно для заполнения'
    },
  },
};
</script>
