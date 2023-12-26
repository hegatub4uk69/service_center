<template>
  <v-container>
    <v-row justify="center" dense="">
      <v-col lg="4">
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
                  clearable
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
                  lines="two"
                  density="compact"
                  nav
                >
                  <v-list-item
                    v-for="(item, i) in items"
                    :key="i"
                    :value="item"
                    color="primary"
                    :disabled="this.selectedIndex > -1"
                    @click="test(item?.raw?.id, item?.raw?.phone, item?.raw?.full_name, i)"
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
      <v-col lg="4">
        <v-card>
          <v-toolbar>
            <v-toolbar-title style="font-size: 25px">
              <v-icon class="mb-1 mr-1" icon="mdi-account-plus-outline"></v-icon>
              Добавление клиента
            </v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-text-field
              v-model="last_name"
              label="Фамилия"
            ></v-text-field>
            <v-text-field
              v-model="first_name"
              label="Имя"
            ></v-text-field>
            <v-text-field
              v-model="father_name"
              label="Отчество"
            ></v-text-field>
            <v-text-field
              v-model="myVal"
              v-mask:[options]="bindedObject"
              label="Номер телефона"
            ></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-btn
              density="default"
              color="blue-darken-1"
              variant="outlined"
              @click="btnTest2"
            >
              Очистить
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
              density="default"
              color="blue-darken-1"
              variant="outlined"
              @click="btnTest"
            >
              Добавить
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import API from "@/axios";
import router from "@/router";
import {store} from "@/store";
import {toast} from "vue3-toastify";
import "vue3-toastify/dist/index.css"
import {vMaska} from "maska";

export default {
  data() {
    return {
      options: {
        mask: "+7 (###) ###-##-##",
      },
      testVal: '',
      testVal2: '',
      last_name: '',
      first_name: '',
      father_name: '',
      myVal: '+79909786738',
      search: '',
      clients: [],
      loadingList: true,
      selectedIndex: -1
    }
  },
  directives: {
    "mask": vMaska
  },
  methods: {
    onClickSeeAll() {
      this.itemsPerPage = this.itemsPerPage === 4 ? this.mice.length : 4
    },
    loadClients() {
      API.post('get-clients')
        .then(response => {
          this.clients = response.data.result
        }).catch(function (error) {
        if (error.response) {
          router.push({name: 'login'})
          store.dispatch('userLogout')
        }
      })
    },
    test(id, phone, full_name, i) {
      toast('Вы выбрали клиента с идентификатором: ' + id + ' ' +
        'Фамилией: ' + full_name.split(' ')[0] + ' ' + 'Именем: ' + full_name.split(' ')[1]+ ' ' +
        'Отчеством: ' + full_name.split(' ')[2], {
        autoClose: 4000,
        theme: "colored",
        type: 'success',
        duration: 5000,
        position: "top-right",
        closeButton: false,
      })
      this.last_name = full_name.split(' ')[0]
      this.first_name = full_name.split(' ')[1]
      this.father_name = full_name.split(' ')[2]
      this.myVal = phone
      this.selectedIndex = i
    },
    btnTest() {
      this.testVal2 = this.myVal.replace(/[^0-9+]/g, '')
      toast('Полученный номер: ' + this.testVal2, {
        autoClose: 4000,
        theme: "colored",
        type: 'success',
        duration: 5000,
        position: "top-right",
        closeButton: false,
      })
    },
    btnTest2() {
      this.last_name = null
      this.first_name = null
      this.father_name = null
      this.myVal = null
      this.selectedIndex = -1
    }
  },
}
</script>

<style>

</style>
