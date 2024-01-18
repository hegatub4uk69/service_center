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
        @click="dialog_add_staff = true"
    >Добавить
    </v-btn>
    <v-dialog
        v-model="dialog_add_staff"
        max-width="600px"
    >
      <v-card title="Добавление сотрудника">
        <template v-slot:prepend>
          <v-icon icon="mdi-plus-box-outline" style="margin-left: 5px"></v-icon>
        </template>
        <v-card-text>
          <v-container>
            <v-row>
              <v-text-field
                  v-model="staffItem.last_name"
                  density="comfortable"
                  label="Фамилия"
              ></v-text-field>
            </v-row>
            <v-row>
              <v-text-field
                  v-model="staffItem.first_name"
                  density="comfortable"
                  label="Имя"
              ></v-text-field>
            </v-row>
            <v-row>
              <v-text-field
                  v-model="staffItem.father_name"
                  density="comfortable"
                  label="Отчество"
              ></v-text-field>
            </v-row>
            <v-row>
              <v-text-field
                  v-model="staffItem.phone_number"
                  v-mask:[options]
                  density="comfortable"
                  label="Номер телефона"
              ></v-text-field>
            </v-row>
            <v-row>
              <v-select
                  v-model="staffItem.post"
                  density="comfortable"
                  :items="posts"
                  label="Должность"
              >
              </v-select>
            </v-row>
            <v-row>
              <v-text-field
                  v-model="accountItem.username"
                  density="comfortable"
                  label="Имя пользователя"
              ></v-text-field>
            </v-row>
            <v-row>
              <v-text-field
                  v-model="accountItem.password"
                  density="comfortable"
                  label="Пароль"
              ></v-text-field>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="blue-darken-1"
              variant="text"
              @click="dialog_add_staff = false"
          >
            Закрыть
          </v-btn>
          <v-btn
              color="blue-darken-1"
              variant="text"
              @click="addStaff"
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
      :items="staff"
      :search="search"
      :items-per-page="10"
      item-value="id"
      class="elevation-1 table"
      @update:options="loadStaff"
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
    <template v-slot:[`item.phone_number`]="{item}">
      <v-text-field
          v-model="item.phone_number"
          v-mask:[options]
          density="compact"
          hide-details
          outlined
      ></v-text-field>
    </template>
    <template v-slot:[`item.post`]="{item}">
      <v-select
          v-model="item.post"
          :items="posts"
          density="compact"
          hide-details
      ></v-select>
    </template>
    <template v-slot:[`item.accounts`]="{item}">
      <v-select
          v-model="item.account_id"
          :items="accounts"
          density="compact"
          hide-details
          item-value="account_id"
          item-title="username"
      >
      </v-select>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon
          size="23px"
          class="me-2 ml-1"
          color="warning"
          icon="mdi-pencil-outline"
          @click="editStaff(item)"
      >
      </v-icon>
      <v-icon
          size="23px"
          color="red"
          icon="mdi-delete-outline"
          @click="deleteStaff(item)"
      >
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
import API from "@/axios";
import {createToast} from "mosha-vue-toastify";
import {vMaska} from "maska";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Staff',
  data() {
    return {
      search: '',
      options: {
        mask: "+7##########",
      },
      dialog_add_staff: false,
      headers: [
        {
          title: 'Действия', key: 'actions',
          fixed: true, sortable: false,
        },
        {title: 'ID', key: 'id',},
        {title: 'Фамилия', key: 'last_name', minWidth: '250px'},
        {title: 'Имя', key: 'first_name', minWidth: '250px'},
        {title: 'Отчество', key: 'father_name', minWidth: '250px'},
        {title: 'Номер телефона', key: 'phone_number', minWidth: '250px'},
        {title: 'Должность', key: 'post', minWidth: '250px'},
        {title: 'Учетная запись', key: 'accounts', minWidth: '250px'},
      ],
      posts: ['Администратор', 'Техник'],
      staff: [],
      accounts: [],
      staffItem: {},
      accountItem: {}
    }
  },
  directives: {
    "mask": vMaska
  },
  methods: {
    loadStaff() {
      API.post('get-staff-adm-panel').then(response => {
        this.staff = response.data.result
      })
      API.post('get-accounts').then(response => {
        this.accounts = response.data.result
      })
    },
    addStaff() {
      API.post('auth/users/', this.accountItem).then(response => {
        this.staffItem.account_id = response.data.id
        API.post('add-staff', this.staffItem).then(response => {
          createToast(response.data.result, {
          showIcon: 'true',
          showCloseButton: false,
          type: 'success',
          position: "top-center",
          timeout: 3000,
          toastBackgroundColor: '#4caf50'
        })
        this.dialog_add_staff = false
        this.loadStaff()
        })
      })
    },
    editStaff(item) {
      API.post('update-staff', {
        id: item.id, last_name: item.last_name, first_name: item.first_name,
        father_name: item.father_name, post: item.post, account_id: item.account_id,
        phone_number: item.phone_number
      }).then(response => {
        createToast(response.data.result, {
          showIcon: 'true',
          showCloseButton: false,
          type: 'success',
          position: "top-center",
          timeout: 3000,
          toastBackgroundColor: '#4caf50'
        })
        this.loadStaff()
      })
    },
    deleteStaff(item) {
      API.post('delete-staff', {id: item.id}).then(response => {
        createToast(response.data.result, {
          showIcon: 'true',
          showCloseButton: false,
          type: 'success',
          position: "top-center",
          timeout: 3000,
          toastBackgroundColor: '#4caf50'
        })
        this.loadStaff()
      })
    }
  }
}
</script>

<style>

</style>
