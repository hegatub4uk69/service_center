<template>
  <v-card-title class="d-flex align-center pe-2">
    <v-text-field
        v-model="search"
        prepend-inner-icon="mdi-magnify"
        density="compact"
        label="Поиск"
        single-line
        flat
        hide-details
        variant="solo-filled"
    ></v-text-field>
    <v-spacer></v-spacer>
    <v-btn
        color="info"
        dark
        variant="outlined"
        @click="dialog_add_order = true"
    >Добавить
    </v-btn>
    <v-dialog
        v-model="dialog_add_order"
        max-width="700px"
    >
      <v-card title="Добавление заказа">
        <template v-slot:prepend>
          <v-icon icon="mdi-text-box-plus-outline" style="margin-left: 5px"></v-icon>
        </template>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col style="padding-left: 0; padding-bottom: 0">
                <v-text-field
                    v-model="orderItem.created_at"
                    type="date"
                    label="Дата оформления"
                >
                </v-text-field>
              </v-col>
              <v-col style="padding-bottom: 0">
                <v-text-field
                    v-model="orderItem.repair_at"
                    type="date"
                    label="Дата ремонта"
                >
                </v-text-field>
              </v-col>
              <v-col style="padding-right: 0; padding-bottom: 0">
                <v-text-field
                    v-model="orderItem.closed_at"
                    type="date"
                    label="Дата выдачи"
                >
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-autocomplete
                  v-model="orderItem.staff_in"
                  :items="staff"
                  color="blue-grey-lighten-2"
                  item-title="full_name"
                  item-value="id"
                  label="Приемщик"
              >
                <template v-slot:item="{ props, item }">
                  <v-list-item
                      v-bind="props"
                      :title="item?.raw?.full_name"
                      :subtitle="item?.raw?.post"
                  ></v-list-item>
                </template>
              </v-autocomplete>
            </v-row>
            <v-row>
              <v-autocomplete
                  v-model="orderItem.executor"
                  :items="staff"
                  color="blue-grey-lighten-2"
                  item-title="full_name"
                  item-value="id"
                  label="Техник"
              >
                <template v-slot:item="{ props, item }">
                  <v-list-item
                      v-bind="props"
                      :title="item?.raw?.full_name"
                      :subtitle="item?.raw?.post"
                  ></v-list-item>
                </template>
              </v-autocomplete>
            </v-row>
            <v-row>
              <v-autocomplete
                  v-model="orderItem.staff_out"
                  :items="staff"
                  color="blue-grey-lighten-2"
                  item-title="full_name"
                  item-value="id"
                  label="Выдал"
              >
                <template v-slot:item="{ props, item }">
                  <v-list-item
                      v-bind="props"
                      :title="item?.raw?.full_name"
                      :subtitle="item?.raw?.post"
                  ></v-list-item>
                </template>
              </v-autocomplete>
            </v-row>
            <v-row>
              <v-text-field
                  v-model="orderItem.title"
                  label="Наименование техники"
              ></v-text-field>
            </v-row>
            <v-row>
              <v-select
                  v-model="orderItem.category_id"
                  :items="categories"
                  item-title="name"
                  item-value="id"
                  label="Категория техники"
              >
              </v-select>
            </v-row>
            <v-row>
              <v-autocomplete
                  v-model="orderItem.client_id"
                  :items="clients"
                  color="blue-grey-lighten-2"
                  item-title="phone"
                  item-value="id"
                  label="Клиент"
              >
                <template v-slot:item="{ props, item }">
                  <v-list-item
                      v-bind="props"
                      prepend-icon="mdi-account-circle-outline"
                      :title="item?.raw?.full_name"
                      :subtitle="item?.raw?.phone"
                  ></v-list-item>
                </template>
              </v-autocomplete>
            </v-row>
            <v-row>
              <v-select
                  v-model="orderItem.status"
                  :items="statuses"
                  label="Статус"
              ></v-select>
            </v-row>
            <v-row>
              <v-textarea
                  v-model="orderItem.description"
                  label="Описание"
              ></v-textarea>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="blue-darken-1"
              variant="text"
              @click="dialog_add_order = false"
          >
            Закрыть
          </v-btn>
          <v-btn
              color="blue-darken-1"
              variant="text"
              @click="addOrder"
          >
            Добавить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card-title>
  <v-divider></v-divider>
  <v-data-table
      :headers="headers"
      :items="orders"
      :search="search"
      :items-per-page="10"
      item-value="id"
      class="elevation-1 table"
      @update:options="loadOrders"
  >
    <!--    <template v-slot:[`header.title`]>
          <span style="padding-right: 500px">Test</span>
        </template>-->
    <template v-slot:[`item.title`]="{item}">
      <v-text-field
          v-model="item.title"
          density="compact"
          hide-details
          outlined
      ></v-text-field>
    </template>
    <template v-slot:[`item.category`]="{item}">
      <v-select
          v-model="item.category"
          :items="categories"
          density="compact"
          hide-details
          item-title="name"
          item-value="id"
      >
      </v-select>
    </template>
    <template v-slot:[`item.status`]="{item}">
      <v-select
          v-model="item.status"
          :items="statuses"
          density="compact"
          hide-details
      ></v-select>
    </template>
    <template v-slot:[`item.client`]="{item}">
      <v-autocomplete
          v-model="item.client"
          :items="clients"
          hide-details
          density="compact"
          color="blue-grey-lighten-2"
          item-title="phone"
          item-value="id"
      >
        <template v-slot:item="{ props, item }">
          <v-list-item
              v-bind="props"
              :title="item?.raw?.full_name"
              :subtitle="item?.raw?.phone"
          ></v-list-item>
        </template>
      </v-autocomplete>
    </template>
    <template v-slot:[`item.staff_in`]="{item}">
      <v-autocomplete
          v-model="item.staff_in"
          :items="staff"
          hide-details
          density="compact"
          color="blue-grey-lighten-2"
          item-title="full_name"
          item-value="id"
      >
        <template v-slot:item="{ props, item }">
          <v-list-item
              v-bind="props"
              :title="item?.raw?.full_name"
              :subtitle="item?.raw?.post"
          ></v-list-item>
        </template>
      </v-autocomplete>
    </template>
    <template v-slot:[`item.executor`]="{item}">
      <v-autocomplete
          v-model="item.executor"
          :items="staff"
          hide-details
          density="compact"
          color="blue-grey-lighten-2"
          item-title="full_name"
          item-value="id"
      >
        <template v-slot:item="{ props, item }">
          <v-list-item
              v-bind="props"
              :title="item?.raw?.full_name"
              :subtitle="item?.raw?.post"
          ></v-list-item>
        </template>
      </v-autocomplete>
    </template>
    <template v-slot:[`item.staff_out`]="{item}">
      <v-autocomplete
          v-model="item.staff_out"
          :items="staff"
          hide-details
          density="compact"
          color="blue-grey-lighten-2"
          item-title="full_name"
          item-value="id"
      >
        <template v-slot:item="{ props, item }">
          <v-list-item
              v-bind="props"
              :title="item?.raw?.full_name"
              :subtitle="item?.raw?.post"
          ></v-list-item>
        </template>
      </v-autocomplete>
    </template>
    <template v-slot:[`item.created_at`]="{item}">
      <v-text-field
          v-model="item.created_at"
          type="date"
          density="compact"
          hide-details
          outlined
      ></v-text-field>
    </template>
    <template v-slot:[`item.repair_at`]="{item}">
      <v-text-field
          v-model="item.repair_at"
          density="compact"
          type="date"
          hide-details
          outlined
      ></v-text-field>
    </template>
    <template v-slot:[`item.closed_at`]="{item}">
      <v-text-field
          v-model="item.closed_at"
          density="compact"
          type="date"
          hide-details
          outlined
      ></v-text-field>
    </template>
    <template v-slot:[`item.description`]="{item}">
      <v-textarea
          v-model="item.description"
          density="compact"
          rows="1"
          hide-details
      >
      </v-textarea>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon
          size="23px"
          class="me-2 ml-1"
          color="warning"
          icon="mdi-pencil-outline"
          @click="editOrder(item)"
      >
      </v-icon>
      <v-icon
          size="23px"
          color="red"
          icon="mdi-delete-outline"
          @click="deleteOrder(item)"
      >
      </v-icon>
    </template>
  </v-data-table>

</template>

<script>
import 'mosha-vue-toastify/dist/style.css';
import API from "@/axios";
import {createToast} from "mosha-vue-toastify";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Orders',
  data() {
    return {
      search: '',
      dialog_add_order: false,
      statuses: ['Новый', 'В работе', 'Готов', 'Выдан'],
      headers: [
        {
          title: 'Действия', key: 'actions',
          fixed: true, sortable: false,
        },
        {title: 'ID', key: 'id',},
        {title: 'Наименование техники', key: 'title', minWidth: '250px'},
        {title: 'Категория', key: 'category', minWidth: '200px'},
        {title: 'Статус', key: 'status', minWidth: '165px'},
        {title: 'Клиент', key: 'client', minWidth: '250px'},
        {title: 'Приемщик', key: 'staff_in', minWidth: '350px'},
        {title: 'Техник', key: 'executor', minWidth: '350px'},
        {title: 'Выдал', key: 'staff_out', minWidth: '350px'},
        {title: 'Дата создания', key: 'created_at', minWidth: '180px'},
        {title: 'Дата ремонта', key: 'repair_at', minWidth: '180px'},
        {title: 'Дата выдачи', key: 'closed_at', minWidth: '180px'},
        {title: 'Описание', key: 'description', minWidth: '450px'},
      ],
      orders: [],
      orderItem: {},
      categories: [],
      clients: [],
      staff: []
    }
  },
  mounted() {
    this.loadCategories()
    this.loadClients()
    this.loadStaff()
  },
  methods: {
    loadOrders() {
      API.post('get-orders-for-adm').then(response => {
        this.orders = response.data.result
      })
    },
    loadCategories() {
      API.post('get-categories').then(response => {
        this.categories = response.data.result
      })
    },
    loadClients() {
      API.post('get-clients').then(response => {
        this.clients = response.data.result
      })
    },
    loadStaff() {
      API.post('get-staff').then(response => {
        this.staff = response.data.result
      })
    },
    addOrder() {
      API.post('add-order-adm', this.orderItem).then(response => {
        createToast(response.data.result, {
          showIcon: 'true',
          showCloseButton: false,
          type: 'success',
          position: "top-center",
          timeout: 3000,
          toastBackgroundColor: '#4caf50'
        })
        this.dialog_add_order = false
        this.loadOrders()
      })
    },
    editOrder(item) {
      API.post('update-order-adm', {
        id: item.id, title: item.title, status: item.status, description: item.description,
        category_id: item.category, client_id: item.client, staff_in: item.staff_in, executor: item.executor,
        staff_out: item.staff_out, created_at: item.created_at, repair_at: item.repair_at, closed_at: item.closed_at
      }).then(response => {
        createToast(response.data.result, {
          showIcon: 'true',
          showCloseButton: false,
          type: 'success',
          position: "top-center",
          timeout: 3000,
          toastBackgroundColor: '#4caf50'
        })
        this.loadOrders()
      })
    },
    deleteOrder(item) {
      API.post('delete-order', {id: item.id}).then(response => {
        createToast(response.data.result, {
          showIcon: 'true',
          showCloseButton: false,
          type: 'success',
          position: "top-center",
          timeout: 3000,
          toastBackgroundColor: '#4caf50'
        })
        this.loadOrders()
      })
    }
  }
}
</script>

<style>
.table {
  background: #fff;
  /*border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;*/
  font-size: 16px;
  white-space: normal;
}
</style>
