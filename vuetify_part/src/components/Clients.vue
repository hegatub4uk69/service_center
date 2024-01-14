<template>
  <v-card flat>
    <v-card-title class="d-flex align-center pe-2">
      <v-dialog v-model="dialog_add_client" width="500px">
        <v-card>
          <v-toolbar>
            <v-toolbar-title style="font-size: 25px">
              <v-icon class="mb-1 mr-1" icon="mdi-account-plus-outline"></v-icon>
              Добавление клиента
            </v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-text-field
              v-model="clientData.last_name"
              label="Фамилия"
              clearable="true"
            ></v-text-field>
            <v-text-field
              v-model="clientData.first_name"
              label="Имя"
              clearable="true"
            ></v-text-field>
            <v-text-field
              v-model="clientData.father_name"
              label="Отчество"
              clearable="true"
            ></v-text-field>
            <v-text-field
              v-model="clientData.phone_number"
              v-mask:[options]
              label="Номер телефона"
              clearable="true"
            ></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              style="margin-bottom: 4px"
              density="default"
              color="blue-darken-1"
              variant="outlined"
              @click="dialog_add_client = false"
            >
              Закрыть
            </v-btn>
            <v-btn
              style="margin-bottom: 4px"
              density="default"
              color="blue-darken-1"
              variant="outlined"
              @click="addClient"
            >
              Добавить
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
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
        @click="dialog_add_client = true"
      >Добавить
      </v-btn>
    </v-card-title>
    <v-divider></v-divider>
    <v-data-table
      :headers="headers"
      :items="clients"
      :search="search"
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
          @click="editClient(item)"
        >
        </v-icon>
        <v-icon
          size="small"
          color="red"
          icon="mdi-delete-outline"
          @click="deleteClient(item)"
        >
        </v-icon>
      </template>
    </v-data-table>
  </v-card>
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
      search: '',
      options: {
        mask: "+7##########",
      },
      dialog_add_client: false,
      headers: [
        {title: 'ID', key: 'id', width: 50},
        {title: 'Фамилия', key: 'last_name', width: 350},
        {title: 'Имя', key: 'first_name', width: 350},
        {title: 'Отчество', key: 'father_name', width: 350},
        {title: 'Телефон', key: 'phone', width: 350},
        {title: 'Действия', key: 'actions', align: 'center', sortable: false, width: 120},
      ],
      clients: [],
      clientData: {
        last_name: null,
        first_name: null,
        father_name: null,
        phone_number: null,
      }
    }
  },
  directives: {
    "mask": vMaska
  },
  methods: {
    editClient(item) {
      API.post('update-client', {
        id: item.id, last_name: item.last_name, first_name: item.first_name,
        father_name: item.father_name, phone_number: item.phone
      })
        .then(response => {
          createToast(response.data.result, {
            showIcon: 'true',
            showCloseButton: false,
            type: 'success',
            position: "top-center",
            timeout: 3000,
            toastBackgroundColor: '#4caf50'
          })
          this.loadClients()
        })
    },
    loadClients() {
      API.post('get-clients-for-adm')
        .then(response => {
          this.clients = response.data.result
        })
    },
    addClient() {
      API.post('add-client', this.clientData)
        .then(response => {
          this.dialog_add_client = false
          createToast(response.data.result, {
            showIcon: 'true',
            showCloseButton: false,
            type: 'success',
            position: "top-center",
            timeout: 3000,
            toastBackgroundColor: '#4caf50'
          })
          this.dialog_add_client = false
          this.loadClients()
        })
    },
    deleteClient(item) {
      API.post('delete-client', {id: item.id})
        .then(response => {
          createToast(response.data.result, {
            showIcon: 'true',
            showCloseButton: false,
            type: 'success',
            position: "top-center",
            timeout: 3000,
            toastBackgroundColor: '#4caf50'
          })
          this.loadClients()
        })
    }
  },
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
