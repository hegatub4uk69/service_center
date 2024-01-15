<template>
  <v-card>
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
      <template v-slot:[`item.title`]="{item}">
        <v-text-field
          v-model="item.title"
          density="compact"
          hide-details
          outlined
        ></v-text-field>
      </template>
      <template v-slot:[`item.category`]="{item}">
        <v-text-field
          v-model="item.category"
          density="compact"
          hide-details
          outlined
        ></v-text-field>
      </template>
      <template v-slot:[`item.status`]="{item}">
        <v-text-field
          v-model="item.status"
          density="compact"
          hide-details
          outlined
        ></v-text-field>
      </template>
      <template v-slot:[`item.client`]="{item}">
        <v-text-field
          v-model="item.client"
          density="compact"
          hide-details
          outlined
        ></v-text-field>
      </template>
      <template v-slot:[`item.staff_in`]="{item}">
        <v-text-field
          v-model="item.staff_in"
          density="compact"
          hide-details
          outlined
        ></v-text-field>
      </template>
      <template v-slot:[`item.executor`]="{item}">
        <v-text-field
          v-model="item.executor"
          density="compact"
          hide-details
          outlined
        ></v-text-field>
      </template>
      <template v-slot:[`item.staff_out`]="{item}">
        <v-text-field
          v-model="item.staff_out"
          density="compact"
          hide-details
          outlined
        ></v-text-field>
      </template>
      <template v-slot:[`item.created_at`]="{item}">
        <v-text-field
          v-model="item.created_at"
          density="compact"
          hide-details
          outlined
        ></v-text-field>
      </template>
      <template v-slot:[`item.repair_at`]="{item}">
        <v-text-field
          v-model="item.repair_at"
          density="compact"
          hide-details
          outlined
        ></v-text-field>
      </template>
      <template v-slot:[`item.closed_at`]="{item}">
        <v-text-field
          v-model="item.closed_at"
          density="compact"
          hide-details
          outlined
        ></v-text-field>
      </template>
      <template v-slot:[`item.description`]="{item}">
        <v-text-field
          v-model="item.description"
          density="compact"
          hide-details
          outlined
        ></v-text-field>
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
  </v-card>
</template>

<script>
import 'mosha-vue-toastify/dist/style.css';
import API from "@/axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Orders',
  data() {
    return {
      search: '',
      dialog_add_order: false,
      headers: [
        {title: 'Действия', key: 'actions', fixed: true, sortable: false},
        {title: 'ID', key: 'id'},
        {title: 'Наименование техники', key: 'title', width: 17999999},
        {title: 'Категория', key: 'category', width: 17999999},
        {title: 'Статус', key: 'status', width: 5000000},
        {title: 'Клиент', key: 'client', width: 50000000},
        {title: 'Приемщик', key: 'staff_in', width: 50000000},
        {title: 'Техник', key: 'executor', width: 50000000},
        {title: 'Выдал', key: 'staff_out', width: 50000000},
        {title: 'Дата создания', key: 'created_at', width: 9000000},
        {title: 'Дата ремонта', key: 'repair_at', width: 9000000},
        {title: 'Дата выдачи', key: 'closed_at', width: 9000000},
        {title: 'Описание', key: 'description', width: 50000000},
        {title: '', width: 1}
      ],
      orders: [],

    }
  },
  methods: {
    loadOrders() {
      API.post('get-orders-for-adm').then(response => {
        this.orders = response.data.result
      })
    },
    addOrder() {
      //
    },
    editOrder() {
      //
    },
    deleteOrder() {
      //
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
}
</style>
