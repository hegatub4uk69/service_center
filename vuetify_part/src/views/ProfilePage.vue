<template>
  <v-container fluid="">
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4" lg="12">
        <v-container fluid="">
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
                            :model-value="'Количество взятых заказов: ' + orders_count.orders_done"
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
                    <v-expansion-panel-title>
                      <template v-slot:default="{ expanded }">
                        <v-row>
                          <v-col cols="2" class="d-flex justify-start align-center">
                            <v-icon style="margin-right: 5px" size="35px" icon="mdi-book-open-outline"></v-icon>
                            <h3>Мои заказы</h3>
                          </v-col>
                          <v-col cols="8" class="d-flex align-center" style="padding-bottom: 0">
                            <v-fade-transition>
                              <v-row align="center" justify="center">
                                <v-col cols="3" style="padding-bottom: 0">
                                  <v-select
                                    v-if="expanded"
                                    v-model="selected_status"
                                    :items="statuses"
                                    density="default"
                                    color="blue"
                                    label="Фильтрация по статусу"
                                    @click.stop="disable_panel = true"
                                  ></v-select>
                                </v-col>
                                <v-col cols="6" style="padding-bottom: 0; padding-top: 0">
                                  <v-text-field
                                    v-if="expanded"
                                    v-model="search"
                                    color="blue"
                                    density="default"
                                    style="height: 90px; padding-bottom: 0; padding-top: 12px"
                                    prepend-inner-icon="mdi-table-search"
                                    label="Введите поисковое значение"
                                    single-line
                                    @click.stop
                                  ></v-text-field>
                                </v-col>
                              </v-row>
                            </v-fade-transition>
                          </v-col>
                        </v-row>
                      </template>
                    </v-expansion-panel-title>
                    <v-expansion-panel-text id="exp-panel">
                      <v-data-table
                        :headers="tableHeaders"
                        :items="orders"
                        :loading="loadingTable"
                        :search="search"
                        id="exp-panel-table"
                        item-value="id"
                        class="elevation-1"
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
                            :text="btn_name"
                            color="success"
                            variant="outlined"
                            @click="orderDoneOrOut(item)"
                          >
                          </v-btn>
                        </template>
                      </v-data-table>
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
import {createToast} from "mosha-vue-toastify";

export default {
  name: 'ProfilePage',
  computed: {
    ...mapState(['user_data']),
    staff_id() {
      return this.$store.state.user_data.staff_id
    },
    btn_name() {
      if (this.selected_status === 'В работе') {
        return 'Готов'
      } else if (this.selected_status === 'Готов') {
        return 'Выдать'
      } else {
        return 'Готов'
      }
    },
  },

  data() {
    return {
      search: '',
      panel: ['user'],
      disable_panel: false,
      selected_status: 'В работе',
      status_to_resp: 'В работе',
      statuses: ['В работе', 'Готов', 'Выдан'],
      tableHeaders: [
        {title: '№', align: 'start', key: 'id'},
        {title: 'Наименование техники', key: 'title'},
        {title: 'Категория', key: 'categoryTitle'},
        {title: 'Клиент', key: 'client_FN'},
        {title: 'Телефон клиента', key: 'client_phone'},
        {title: 'Статус', key: 'status', align: 'start'},
        {title: 'Действия', key: 'actions', sortable: false}
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
  watch: {
    staff_id(val) {
      this.ordersStat(val)
    },
    selected_status() {
      if ((this.selected_status === 'В работе' || 'Готов') && !this.tableHeaders[6]) {
        this.tableHeaders.push({title: 'Действия', key: 'actions', sortable: false})
      } else if (this.selected_status === 'Выдан' && this.tableHeaders[6]) {
        this.tableHeaders.splice(6)
      }
      this.status_to_resp = this.selected_status
      this.loadTableItems()
    },
  },

  mounted() {
    if (this.staff_id) {
      this.ordersStat(this.staff_id)
    }
  },

  methods: {
    loadTableItems() {
      this.loadingTable = true
      API.post('get-my-orders', {executor_id: this.$store.state.user_data.staff_id, status: this.status_to_resp})
        .then(response => {
          this.orders = response.data.result
          this.loadingTable = false
        })
    },
    ordersStat(staff_id) {
      API.post('get-my-orders-count', {staff_id: staff_id})
        .then(response => {
          this.orders_count.orders_in = response.data.result.orders_in
          this.orders_count.orders_done = response.data.result.orders_done
          this.orders_count.orders_out = response.data.result.orders_out
        })
    },
    orderDoneOrOut(item) {
      let date = new Date();
      if (this.selected_status === 'В работе') {
        API.post('order-done', {
          id: item.id,
          status: 'Готов',
          repair_at: date.toLocaleDateString('ru-RU')
        }).then(response => {
          createToast(response.data.result, {
            showIcon: 'true',
            showCloseButton: false,
            type: 'danger',
            position: "top-center",
            timeout: 3000,
            toastBackgroundColor: '#4caf50'
          })
          this.loadTableItems()
        })
      } else if (this.selected_status === 'Готов') {
        API.post('order-out', {
          id: item.id,
          status: 'Выдан',
          closed_at: date.toLocaleDateString('ru-RU'),
          staff_out: this.$store.state.user_data.staff_id
        }).then(response => {
          createToast(response.data.result, {
            showIcon: 'true',
            showCloseButton: false,
            type: 'danger',
            position: "top-center",
            timeout: 3000,
            toastBackgroundColor: '#4caf50'
          })
          this.loadTableItems()
        })
      }
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

<style lang="scss">
#exp-panel > * {
  padding: 0;
}
#exp-panel-table {
  font-size: 15px;
}
</style>
