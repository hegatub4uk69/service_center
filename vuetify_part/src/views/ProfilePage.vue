<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4" lg="10">
        <v-container>
          <v-row dense>
            <v-col>
              <v-card elevation="5">
                <v-expansion-panels variant="accordion">
                  <v-expansion-panel>
                    <template v-slot:title>
                      <v-icon style="margin-right: 5px" size="35px" icon="mdi-card-account-details-outline"></v-icon>
                      <h3>Информация о пользователе</h3>
                    </template>
                    <v-expansion-panel-text>
                      <div class="d-flex flex-no-wrap">
                        <v-avatar
                          class="ma-3"
                          size="125"
                          rounded="0"
                        >
                          <v-img src="/free-icon-avatar-8727604.png"></v-img>
                        </v-avatar>
                        <v-card-text>
                          <v-card-title>Личная информация</v-card-title>
                          <v-divider style="padding-bottom: 20px"></v-divider>
                          <v-text-field
                            label="Фамилия Имя Отчество"
                            :model-value="user_data.staff_full_name"
                          >
                            <template v-slot:prepend-inner>
                              <v-icon
                                style="margin-left: 3px; margin-right: 10px"
                                icon="mdi-card-account-details-outline"></v-icon>
                            </template>
                          </v-text-field>
                          <v-text-field
                            label="Логин"
                            :model-value="user_data.login"
                          >
                            <template v-slot:prepend-inner>
                              <v-icon
                                style="margin-left: 3px; margin-right: 10px"
                                icon="mdi-alpha-l-box-outline"></v-icon>
                            </template>
                          </v-text-field>
                          <v-text-field
                            label="Номер телефона"
                            :model-value="user_data.staff_phone"
                          >
                            <template v-slot:prepend-inner>
                              <v-icon
                                style="margin-left: 3px; margin-right: 10px"
                                icon="mdi-phone-outline"></v-icon>
                            </template>
                          </v-text-field>
                        </v-card-text>
                        <v-card-text>
                          <v-card-title>Статистика заказов</v-card-title>
                          <v-divider style="padding-bottom: 20px"></v-divider>
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
                    </v-expansion-panel-text>
                  </v-expansion-panel>
                  <v-expansion-panel>
                    <template v-slot:title>
                      <v-icon style="margin-right: 5px" size="35px" icon="mdi-book-open-outline"></v-icon>
                      <h3>Мои заказы</h3>
                    </template>
                    <v-expansion-panel-text>
                      <div class="d-flex flex-no-wrap">
                        <v-data-table
                          :headers="tableHeaders"
                        >
                        </v-data-table>
                      </div>
                    </v-expansion-panel-text>
                  </v-expansion-panel>
                </v-expansion-panels>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import {mapState} from "vuex";

export default {
  name: 'ProfilePage',
  computed: mapState(['user_data']),
  data() {
    return {
      tableHeaders: [
        {title: '№', align: 'start', key: 'id'},
        {title: 'Наименование техники', key: 'title'},
        {title: 'Категория', key: 'categoryTitle'},
        {title: 'Клиент', key: 'client_FN'},
        {title: 'Телефон клиента', key: 'client_phone'},
        {title: 'Статус', key: 'status', align: 'start'},
        {title: 'Действия', key: 'actions', sortable: false},
      ],
    }
  },
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

<style>
</style>
