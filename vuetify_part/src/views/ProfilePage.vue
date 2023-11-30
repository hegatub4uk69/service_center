<template>
  <v-container>
    <v-row>
      <v-col>
        <v-container>
          <v-row dense>
            <v-col>
              <v-card elevation="5" style="width: 750px">
                <div class="d-flex flex-no-wrap">
                  <v-avatar
                    class="ma-3"
                    size="125"
                    rounded="0"
                  >
                    <v-img src="/kompyuternyj-servis.png"></v-img>
                  </v-avatar>
                  <v-card-text>
                    <v-text-field
                      label="Фамилия Имя Отчество"
                      model-value="Крылов Олег Геннадьевич"
                    >
                      <template v-slot:prepend-inner>
                        <v-icon
                          style="margin-left: 3px; margin-right: 10px"
                          icon="mdi-card-account-details-outline"></v-icon>
                      </template>
                    </v-text-field>
                    <v-text-field
                      label="Логин"
                      model-value="test_login"
                    >
                      <template v-slot:prepend-inner>
                        <v-icon
                          style="margin-left: 3px; margin-right: 10px"
                          icon="mdi-alpha-l-box-outline"></v-icon>
                      </template>
                    </v-text-field>
                    <v-text-field
                      label="Номер телефона"
                      model-value="+79049873747"
                    >
                      <template v-slot:prepend-inner>
                        <v-icon
                          style="margin-left: 3px; margin-right: 10px"
                          icon="mdi-phone-outline"></v-icon>
                      </template>
                    </v-text-field>
                  </v-card-text>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-col>

      <v-col>
        <v-container>
          <v-row>
            <v-col>
              <v-card
                title="Принятые заказы"
                color="info"
              ></v-card>
            </v-col>
            <v-col>
              <v-card
                title="Исполненные заказы"
                color="purple"
              >
                <div class="d-flex flex-nowrap justify-space-between">
                  <v-icon style="margin-left: 13px" size="50px" icon="mdi-card"></v-icon>
                  <v-text-field style="width: 50px" variant="underlined"></v-text-field>
                </div>
                <v-card-subtitle>test</v-card-subtitle>
              </v-card>
            </v-col>
            <v-col>
              <v-card
                title="Выданные заказы"
                color="success"
              ></v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-col>
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
