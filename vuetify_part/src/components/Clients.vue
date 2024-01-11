<template>
  <v-data-table
    :headers="headers"
    :items="clients"
    :items-per-page="10"
    item-value="id"
    class="elevation-1 table"
    @update:options="loadClients"
  >
    <template v-slot:[`item.last_name`]="{item}">
      <v-text-field
        v-model="item.last_name"
        density="compact"
        hide-details
        outlined
      ></v-text-field>
    </template>
    <template v-slot:[`item.first_name`]="{item}">
      <v-text-field
        v-model="item.first_name"
        density="compact"
        hide-details
        outlined
      ></v-text-field>
    </template>
    <template v-slot:[`item.father_name`]="{item}">
      <v-text-field
        v-model="item.father_name"
        density="compact"
        hide-details
        outlined
      ></v-text-field>
    </template>
    <template v-slot:[`item.phone`]="{item}">
      <v-text-field
        v-model="item.phone"
        v-mask:[options]
        density="compact"
        hide-details
        outlined
      ></v-text-field>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon
        size="small"
        class="me-2"
        color="warning"
        icon="mdi-pencil-outline"
        @click="getdata(item)"
      >
      </v-icon>
      <v-icon
        size="small"
        color="red"
        icon="mdi-delete-outline"
      >
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
import {createToast} from "mosha-vue-toastify";
import 'mosha-vue-toastify/dist/style.css';
import {vMaska} from "maska";
import API from "@/axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Staff',
  data() {
    return {
      options: {
        mask: "+7 (###) ###-##-##",
      },
      headers: [
        {title: 'ID', key: 'id', width: 50},
        {title: 'Фамилия', key: 'last_name', width: 350},
        {title: 'Имя', key: 'first_name', width: 350},
        {title: 'Отчество', key: 'father_name', width: 350},
        {title: 'Телефон', key: 'phone', width: 350},
        {title: 'Действия', key: 'actions', align: 'center', sortable: false, width: 120},
      ],
      clients: [],
    }
  },
  directives: {
    "mask": vMaska
  },
  methods: {
    getdata(item) {
      createToast(item.id + item.last_name + item.first_name + item.father_name + item.phone, {
        showIcon: 'true',
        showCloseButton: false,
        type: 'success',
        position: "top-center",
        timeout: 3000,
        toastBackgroundColor: '#4caf50'
      })
    },
    loadClients() {
      API.post('get-clients-for-adm')
        .then(response => {
          this.clients = response.data.result
        })
    },
  },
}
</script>

<style>
.table {
  background: #fff;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
  font-size: 16px;
}
</style>
