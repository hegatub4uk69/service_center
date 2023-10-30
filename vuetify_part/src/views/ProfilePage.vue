<template>
  <v-container>
    <v-row align="center" justify="center" dense="">
      <v-card elevation="5" style="width: 880px">
        <v-row align="center" justify="center" dense="">
          <v-col class="px-5" cols="12" sm="8" md="8" lg="8">
            <v-card-text>
              <v-img
                class="mx-16"
                :width="350"
                src="/kompyuternyj-servis.png"
              ></v-img>
              <v-chip-group>
                <v-chip class="chips" label>
                  <v-icon start="" icon="mdi-card-account-details-outline"></v-icon>
                  Фамилия Имя Отчество
                </v-chip>
                <v-chip class="chips" label>
                  <v-icon start="" icon="mdi-alpha-l-box-outline"></v-icon>
                  Логин
                </v-chip>
                <v-chip class="chips" label>
                  <v-icon start="" icon="mdi-phone-outline"></v-icon>
                  Номер телефона
                </v-chip>
                <v-chip class="chips" label>
                  <v-icon start="" icon="mdi-notebook-plus-outline"></v-icon>
                  Количество принятых заказов: 5
                </v-chip>
                <v-chip class="chips" label>
                  <v-icon start="" icon="mdi-notebook-check-outline"></v-icon>
                  Количество закрытых заказов: 3
                </v-chip>
              </v-chip-group>
            </v-card-text>
          </v-col>
        </v-row>
      </v-card>
    </v-row>
  </v-container>
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

<style scoped>
.chips {
  font-size: 25px;
  width: 500px;
  height: 50px;
}
</style>
