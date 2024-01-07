<template>
  <v-container>
    <v-row justify="center" dense="">
      <v-col lg="6">
        <v-card>
          <v-data-iterator
            :items="clients"
            :items-per-page="5"
            :search="search"
            @update:options="loadClients"
          >
            <template v-slot:header>
              <v-toolbar>
                <v-toolbar-title style="font-size: 25px">
                  <v-icon class="mb-1 mr-1" icon="mdi-account-group-outline"></v-icon>
                  Клиенты
                </v-toolbar-title>
                <v-spacer></v-spacer>
                <v-text-field
                  class="px-2"
                  v-model="search"
                  clearable="true"
                  density="comfortable"
                  hide-details
                  placeholder="Поиск"
                  prepend-inner-icon="mdi-magnify"
                  style="max-width: 300px;"
                  variant="solo"
                ></v-text-field>
              </v-toolbar>
            </template>

            <template v-slot:default="{ items }">
              <v-container class="pa-2" fluid>
                <v-list
                  id="list"
                  lines="two"
                  density="compact"
                  nav
                >
                  <v-list-item
                    v-for="(item, i) in items"
                    color="primary"
                    :key="i"
                    :value="item"
                    :active="item.value === currentlyActiveItem.value"
                    @click="toUpdateClient(item?.raw?.id, item?.raw?.phone, item?.raw?.full_name, i, item)"
                  >
                    <template v-slot:prepend>
                      <v-icon
                        style="font-size: 40px"
                        icon="mdi-account-circle-outline">
                      </v-icon>
                    </template>
                    <template v-slot:title>
                      <v-list-item-title style="font-size: 18px">{{ item?.raw?.full_name }}</v-list-item-title>
                    </template>
                    <template v-slot:subtitle>
                      <v-list-item-subtitle style="font-size: 15px;">{{ item?.raw?.phone }}</v-list-item-subtitle>
                    </template>
                  </v-list-item>
                </v-list>
              </v-container>
            </template>

            <template v-slot:footer="{ page, pageCount, prevPage, nextPage }">
              <div class="d-flex align-center justify-center pa-4">
                <v-btn
                  :disabled="page === 1"
                  icon="mdi-arrow-left"
                  density="comfortable"
                  variant="tonal"
                  rounded
                  @click="prevPage"
                ></v-btn>

                <div class="mx-2 text-caption">
                  <span style="font-size: 15px">Страница {{ page }} из {{ pageCount }}</span>
                </div>

                <v-btn
                  :disabled="page >= pageCount"
                  icon="mdi-arrow-right"
                  density="comfortable"
                  variant="tonal"
                  rounded
                  @click="nextPage"
                ></v-btn>
              </div>
            </template>
          </v-data-iterator>
        </v-card>
      </v-col>
      <v-col lg="6">
        <v-card>
          <v-toolbar>
            <v-toolbar-title style="font-size: 25px">
              <v-icon class="mb-1 mr-1" :icon="formIcon"></v-icon>
              {{ formTitle }}
            </v-toolbar-title>
            <v-btn
              v-if="editStatus"
              icon="mdi-close-outline"
              color="red"
              @click="closeEdit"
              style="font-size: 20px"></v-btn>
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
              v-model="phoneVal"
              v-mask:[options]
              label="Номер телефона"
              clearable="true"
            ></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-btn
              style="margin-bottom: 4px"
              density="default"
              color="blue-darken-1"
              variant="outlined"
              @click="clearForm"
            >
              Очистить
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
              style="margin-bottom: 4px"
              v-if="editStatus"
              density="default"
              color="red-darken-1"
              variant="outlined"
              @click="deleteClient"
            >
              Удалить
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
              style="margin-bottom: 4px"
              density="default"
              color="blue-darken-1"
              variant="outlined"
              @click="actionClient"
            >
              {{ btnFormTitle }}
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import API from "@/axios";
import {createToast} from 'mosha-vue-toastify';
import 'mosha-vue-toastify/dist/style.css'
import "vue3-toastify/dist/index.css"
import {vMaska} from "maska";

export default {
  data() {
    return {
      options: {
        mask: "+7 (###) ###-##-##",
      },
      clientData: {
        id: null,
        last_name: '',
        first_name: '',
        father_name: '',
        phone_number: ''
      },
      phoneVal: '',
      search: '',
      clients: [],
      listItemEl: null,
      editStatus: false,
      loadingList: true,
      selectedIndex: -1,
      clientIdToDelete: null,
      currentlyActiveItem: {
        value: null,
        selectable: false
      },
      pointer: 'none',
    }
  },
  directives: {
    "mask": vMaska
  },
  computed: {
    formTitle() {
      if (this.selectedIndex === -1 && this.editStatus === false) {
        return 'Добавление клиента'
      } else if (this.selectedIndex > -1 && this.editStatus === true) {
        return 'Изменение данных клиента'
      } else return 'Добавление клиента'
    },
    formIcon() {
      if (this.selectedIndex === -1 && this.editStatus === false) {
        return 'mdi-account-plus-outline'
      } else if (this.selectedIndex > -1 && this.editStatus === true) {
        return 'mdi-account-edit-outline'
      } else return 'mdi-account-plus-outline'
    },
    btnFormTitle() {
      if (this.selectedIndex === -1 && this.editStatus === false) {
        return 'Добавить'
      } else if (this.selectedIndex > -1 && this.editStatus === true) {
        return 'Изменить'
      } else return 'Добавить'
    }
  },
  methods: {
    loadClients() {
      API.post('get-clients')
        .then(response => {
          this.clients = response.data.result
        })
    },
    deleteClient() {
      API.post('delete-client', this.clientIdToDelete)
        .then(response => {
          createToast(response.data.result, {
            showIcon: 'true',
            showCloseButton: false,
            type: 'danger',
            position: "top-center",
            timeout: 3000,
            toastBackgroundColor: '#4caf50'
          })
          this.closeEdit()
          this.loadClients()
        })
    },
    actionClient() {
      if (this.editStatus === false) {
        this.clientData.phone_number = this.phoneVal.replace(/[^0-9+]/g, '')
        API.post('add-client', this.clientData)
          .then(response => {
            createToast(response.data.result, {
              showIcon: 'true',
              showCloseButton: false,
              type: 'danger',
              position: "top-center",
              timeout: 3000,
              toastBackgroundColor: '#4caf50'
            })
            this.loadClients()
          })
      } else {
        this.clientData.phone_number = this.phoneVal.replace(/[^0-9+]/g, '')
        API.post('update-client', this.clientData)
          .then(response => {
            createToast(response.data.result, {
              showIcon: 'true',
              showCloseButton: false,
              type: 'danger',
              position: "top-center",
              timeout: 3000,
              toastBackgroundColor: '#4caf50'
            })
            this.loadClients()
          })
      }
    },
    toUpdateClient(id, phone, full_name, i, item) {
      this.currentlyActiveItem = item
      this.editStatus = true
      this.clientData.id = id
      this.clientData.last_name = full_name.split(' ')[0]
      this.clientData.first_name = full_name.split(' ')[1]
      this.clientData.father_name = full_name.split(' ')[2]
      this.phoneVal = phone
      this.clientIdToDelete = {id: item.raw.id}
      this.selectedIndex = i
      this.listItemEl = document.getElementById('list')
      this.listItemEl.style.pointerEvents = 'none'
    },
    closeEdit() {
      this.editStatus = false
      this.clientData.last_name = null
      this.clientData.first_name = null
      this.clientData.father_name = null
      this.phoneVal = null
      this.clientIdToDelete = null
      this.selectedIndex = -1
      this.currentlyActiveItem = {
        value: null,
        selectable: null
      }
      this.listItemEl.style.pointerEvents = 'auto'
    },
    clearForm() {
      this.clientData.last_name = null
      this.clientData.first_name = null
      this.clientData.father_name = null
      this.phoneVal = null
    },
  },
}
</script>

<style>

</style>
