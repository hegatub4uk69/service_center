<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4" lg="10">
        <v-container>
          <v-row dense>
            <v-col>
              <v-card elevation="5">
                <v-expansion-panels v-model="this.panel" variant="accordion">
                  <v-expansion-panel value="user">
                    <template v-slot:title>
                      <v-icon style="margin-right: 5px" size="35px" icon="mdi-card-account-details-outline"></v-icon>
                      <h3>Информация о пользователе</h3>
                    </template>
                    <v-expansion-panel-text>
                      <div class="d-flex flex-no-wrap">
                        <v-avatar
                          class="ma-3"
                          size="160"
                          rounded="0"
                        >
                          <v-card-text>
                            <v-img src="/free-icon-avatar-8727604.png" class="mb-2"></v-img>
                            <v-card elevation="2">
                              {{ user_data.post }}
                            </v-card>
                          </v-card-text>
                        </v-avatar>
                        <v-card-text>
                          <v-card-title>Личная информация</v-card-title>
                          <v-divider style="padding-bottom: 20px"></v-divider>
                          <v-text-field
                            readonly=""
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
                            readonly=""
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
                            readonly=""
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
                            readonly=""
                            class="text-black"
                            :model-value="'Количество принятых заказов: ' + orders_count.orders_in"
                          >
                            <template v-slot:prepend-inner>
                              <v-icon
                                style="margin-left: 3px; margin-right: 10px"
                                icon="mdi-clipboard-text-clock-outline"></v-icon>
                            </template>
                          </v-text-field>
                          <v-text-field
                            readonly=""
                            class="text-black"
                            :model-value="'Количество готовых заказов: ' + orders_count.orders_done"
                          >
                            <template v-slot:prepend-inner>
                              <v-icon
                                style="margin-left: 3px; margin-right: 10px"
                                icon="mdi-toolbox-outline"></v-icon>
                            </template>
                          </v-text-field>
                          <v-text-field
                            readonly=""
                            class="text-black"
                            :model-value="'Количество выданных заказов: ' + orders_count.orders_out"
                          >
                            <template v-slot:prepend-inner>
                              <v-icon
                                style="margin-left: 3px; margin-right: 10px"
                                icon="mdi-check-outline"></v-icon>
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
                          :items="orders"
                          :loading="loadingTable"
                          item-value="id"
                          class="elevation-1 table"
                          @update:options="loadTableItems"
                        >
                          <template v-slot:[`item.status`]="{ value }">
                            <v-chip :color="getColor(value)">
                              {{ value }}
                            </v-chip>
                          </template>
                          <!--Кнопки действий над заказами-->
                          <template v-slot:[`item.actions`]="{ item }">
                            <v-btn
                              color="success"
                              variant="outlined"
                              @click="orderDoneOrOut(item)"
                            >
                            </v-btn>
                          </template>
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
import API from "@/axios";

export default {
  name: 'ProfilePage',
  computed: mapState(['user_data']),
  data() {
    return {
      panel: ['user'],
      tableHeaders: [
        {title: '№', align: 'start', key: 'id'},
        {title: 'Наименование техники', key: 'title'},
        {title: 'Категория', key: 'categoryTitle'},
        {title: 'Клиент', key: 'client_FN'},
        {title: 'Телефон клиента', key: 'client_phone'},
        {title: 'Статус', key: 'status', align: 'start'},
        {title: 'Действия', key: 'actions', sortable: false},
      ],
      orders_count: {
        orders_in: null,
        orders_done: null,
        orders_out: null
      },
      orders: [],
      loadingTable: true,
    }
  },
  mounted() {
  this.ordersStat()
  },
  methods: {
    loadTableItems() {
      this.loadingTable = true
      API.post('get-my-orders', {executor_id: this.$store.state.user_data.staff_id})
        .then(response => {
          this.orders = response.data.result
          this.loadingTable = false
        })
    },
    ordersStat() {
      API.post('get-my-orders-count', {staff_id: this.$store.state.user_data.staff_id})
        .then(response => {
          this.orders_count.orders_in = response.data.result.orders_in
          this.orders_count.orders_done = response.data.result.orders_done
          this.orders_count.orders_out = response.data.result.orders_out
        })
    },
    orderDoneOrOut(item) {
      item
    },
    getColor(status) {
      if (status === 'В работе') return 'orange'
      else if (status === 'Готов') return 'green'
      else if (status === 'Выдан') return 'purple'
      else return 'red'
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
};
</script>

<style>
</style>
