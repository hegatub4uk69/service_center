<template>
  <v-container fluid="" style="height: 80px">
    <v-card style="height: 70px" color="">
      <v-row align="center" justify="center" dense="">
        <v-col cols="4" sm="4" md="4" lg="2">
          <!--Кнопки фильтрации данных в таблице-->
          <v-select
            v-model="selected_status"
            :items="statuses"
            label="Фильтрация по статусу"
          ></v-select>
        </v-col>
        <v-col cols="7" sm="6" md="6" lg="5">
          <!--Поле для поиска данных в таблице-->
          <v-text-field
            v-model="search"
            variant="underlined"
            style="height: 90px"
            prepend-inner-icon="mdi-table-search"
            label="Введите поисковое значение"
            single-line
          ></v-text-field>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
  <v-container fluid="">
    <v-row dense="">
      <v-col>
        <!--Таблица данных заказов-->
        <v-data-table
          :headers="ordersHeaders"
          :search="search"
          :items="orders"
          :loading="loadingTable"
          item-value="id"
          class="elevation-1 table"
          @update:options="loadTableItems"
        >
          <!--Панель инструментов таблицы-->
          <template v-slot:top>
            <v-toolbar flat="" color="white">
              <!--Заголовок таблицы-->
              <v-toolbar-title style="font-size: 25px">
                <v-icon class="mb-1" icon="mdi-book-open-outline"></v-icon>
                Заказы
              </v-toolbar-title>
              <v-spacer></v-spacer>
              <!--Диалоговое окно добавления заказа-->
              <v-dialog
                v-model="dialog"
                max-width="700px"
              >
                <!--Кнопка оформления на панели инструментов таблицы-->
                <template v-slot:activator="{ props }">
                  <v-btn
                    color="purple"
                    dark
                    class="mb-2"
                    v-bind="props"
                    variant="outlined"
                  >Оформить
                  </v-btn>
                </template>
                <!--Элементы диалогового окна-->
                <v-card :title="formTitle">
                  <template v-slot:prepend>
                    <v-icon
                      :icon="formIcon"
                      style="margin-left: 5px"
                    ></v-icon>
                  </template>
                  <template v-if="info" v-slot:append>
                    <v-icon
                      :icon="info ? 'mdi-pencil' : 'mdi-information-outline'"
                      :color="info ? 'orange' : 'blue'"
                      @click="info = !info"
                    >
                    </v-icon>
                  </template>
                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col style="padding-left: 0; padding-bottom: 0">
                          <v-text-field
                            v-if="info"
                            :model-value="editedItem.created_at"
                            label="Дата оформления"
                            :readonly="true"
                          >
                          </v-text-field>
                        </v-col>
                        <v-col style="padding-bottom: 0">
                          <v-text-field
                            v-if="info"
                            :model-value="editedItem.repair_at"
                            label="Дата ремонта"
                            :readonly="true"
                          >
                          </v-text-field>
                        </v-col>
                        <v-col style="padding-right: 0; padding-bottom: 0">
                          <v-text-field
                            v-if="info"
                            :model-value="editedItem.closed_at"
                            label="Дата выдачи"
                            :readonly="true"
                          >
                          </v-text-field>
                        </v-col>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-if="info"
                          :model-value="editedItem.staff_in_FN"
                          label="Приемщик"
                          :readonly="true"
                        >
                        </v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-if="info"
                          :model-value="editedItem.executor_FN"
                          label="Техник"
                          :readonly="true"
                        >
                        </v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-if="info"
                          :model-value="editedItem.staff_out_FN"
                          label="Заказ выдал"
                          :readonly="true"
                        >
                        </v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          :readonly="info"
                          v-model="editedItem.title"
                          label="Наименование техники"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select
                          :readonly="info"
                          v-model="editedItem.category_id"
                          :items="categories"
                          item-title="name"
                          item-value="id"
                          label="Категория техники"
                        >
                        </v-select>
                      </v-row>
                      <!--Выпадающий список с выбором клиента-->
                      <v-row>
                        <v-autocomplete
                          :readonly="info"
                          v-model="editedItem.client_id"
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
                        <v-textarea
                          :readonly="info"
                          v-model="editedItem.description"
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
                      @click="close"
                    >
                      Закрыть
                    </v-btn>
                    <v-btn
                      :disabled="info"
                      color="blue-darken-1"
                      variant="text"
                      @click="save"
                    >
                      {{ buttonTitle }}
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
              <!--Диалоговое окно удаления заказа-->
              <v-dialog v-model="dialogDelete" max-width="520px">
                <v-card
                  title="Вы уверены, что хотите удалить данный заказ?">
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Закрыть</v-btn>
                    <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">Удалить</v-btn>
                    <v-spacer></v-spacer>
                  </v-card-actions>
                </v-card>
              </v-dialog>
              <v-dialog v-model="dialogStaff" max-width="500px">
                <v-card class="align-center"
                        title="Вы уверены, что хотите взять данный заказ?"
                >
                  <v-card-actions>
                    <v-btn color="blue-darken-1" variant="text" @click="takeOrder">Подтвердить</v-btn>
                    <v-btn color="blue-darken-1" variant="text" @click="closeTake">Закрыть</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>
          <!--Цветное выделение статуса заказа-->
          <template v-slot:[`item.status`]="{ value }">
            <v-chip :color="getColor(value)">
              {{ value }}
            </v-chip>
          </template>
          <!--Кнопки действий над заказами-->
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon
              size="small"
              color="purple"
              class="me-2"
              icon="mdi-account-circle-outline"
              @click="editStaff(item)"
            >
            </v-icon>
            <v-icon
              size="small"
              class="me-2"
              color="info"
              icon="mdi-information-outline"
              @click="editItem(item)"
            >
            </v-icon>
            <v-icon
              size="small"
              color="red"
              icon="mdi-delete-outline"
              @click="deleteItem(item)"
            >
            </v-icon>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import API from "@/axios";
import {createToast} from 'mosha-vue-toastify';
import 'mosha-vue-toastify/dist/style.css'

export default {
  data() {
    return {
      dialog: false,
      dialogDelete: false,
      dialogStaff: false,
      search: '',
      info: false,
      orderIdToTake: null,
      selected_status: 'Новый',
      status_to_resp: {
        status: 'Новый'
      },
      statuses: ['Новый', 'В работе', 'Готов', 'Выдан'],
      ordersHeaders: [
        {title: '№', align: 'start', key: 'id'},
        {title: 'Наименование техники', key: 'title'},
        {title: 'Категория', key: 'categoryTitle'},
        {title: 'Клиент', key: 'client_FN'},
        {title: 'Телефон клиента', key: 'client_phone'},
        {title: 'Статус', key: 'status', align: 'start'},
        {title: 'Действия', key: 'actions', sortable: false},
      ],
      editedIndex: -1,
      editedItem: {
        title: '',
        category_id: null,
        status: 'Новый',
        client_id: null,
        staff_in_id: this.$store.state.user_data.staff_id,
        executor_id: null,
        description: '',
        created_at: null,
      },
      defaultItem: {
        title: '',
        category_id: null,
        status: 'Новый',
        client_id: null,
        staff_in_id: this.$store.state.user_data.staff_id,
        description: '',
        created_at: null,
      },
      clients: [],
      orders: [],
      categories: [],
      loadingTable: true,
    }
  },

  computed: {
    formTitle() {
      if (this.editedIndex === -1 && this.info === false) {
        return 'Новый заказ'
      } else if (this.editedIndex > -1 && this.info === false) {
        return 'Изменение данных заказа'
      } else {
        return 'Полная инфомация о заказе'
      }
    },
    formIcon() {
      if (this.editedIndex === -1 && this.info === false) {
        return 'mdi-text-box-plus-outline'
      } else if (this.editedIndex > -1 && this.info === false) {
        return 'mdi-text-box-edit-outline'
      } else {
        return 'mdi-text-box-outline'
      }
    },
    buttonTitle() {
      return this.editedIndex === -1 ? 'Оформить' : 'Изменить'
    }
  },

  watch: {
    selected_status() {
      this.status_to_resp.status = this.selected_status
      this.loadTableItems()
    },
    dialog() {
      if (!this.dialog) {
        this.close();
      } else {
        this.loadSelectCategory();
        this.loadSelectClient();
      }
    },
    dialogDelete(val) {
      val || this.closeDelete()
    },
  },

  methods: {
    loadOtherOrderData(id) {
      API.post('get-order-other-data', id)
        .then(response => {
          this.editedItem = Object.assign(this.editedItem, response.data.result[0])
          this.dialog = true
        })
    },
    loadSelectCategory() {
      API.post('get-categories')
        .then(response => {
          this.categories = response.data.result
        })
    },
    loadSelectClient() {
      API.post('get-clients')
        .then(response => {
          this.clients = response.data.result
        })
    },
    loadTableItems() {
      this.loadingTable = true
      API.post('get-orders', this.status_to_resp)
        .then(response => {
          this.orders = response.data.result
          this.loadingTable = false
        })
    },
    getColor(status) {
      if (status === 'Новый') return 'info'
      else if (status === 'В работе') return 'orange'
      else if (status === 'Готов') return 'green'
      else if (status === 'Выдан') return 'purple'
      else return 'red'
    },
    editStaff(item) {
      this.orderIdToTake = item.id
      this.dialogStaff = true
    },
    editItem(item) {
      this.info = true
      this.editedIndex = this.orders.indexOf(item)
      this.editedItem = {
        id: item.id,
        title: item.title,
      }
      this.loadOtherOrderData(item.id);
    },
    deleteItem(item) {
      this.editedIndex = this.orders.indexOf(item)
      this.editedItem = {id: item.id}
      this.dialogDelete = true
    },
    deleteItemConfirm() {
      API.post('delete-order', this.editedItem)
        .then(response => {
          createToast(response.data.result, {
            showIcon: 'true',
            showCloseButton: false,
            type: 'success',
            position: "top-center",
            timeout: 3000,
            toastBackgroundColor: '#4caf50'
          })
          this.loadTableItems()
        })
      this.closeDelete()
    },
    close() {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
        this.clients = []
        this.categories = []
        this.info = false
      })
    },
    closeDelete() {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    closeTake() {
      this.dialogStaff = false
      this.orderIdToTake = null
    },
    takeOrder() {
      API.post('take-order', {
        id: this.orderIdToTake,
        executor_id: this.$store.state.user_data.staff_id,
        status: 'В работе'})
        .then(response => {
          createToast(response.data.result, {
              showIcon: 'true',
              showCloseButton: false,
              type: 'success',
              position: "top-center",
              timeout: 3000,
              toastBackgroundColor: '#4caf50'
            })
            this.loadTableItems()
        })
      this.closeTake()
    },
    save() {
      if (this.editedIndex > -1) {
        API.post('update-order', this.editedItem)
          .then(response => {
            createToast(response.data.result, {
              showIcon: 'true',
              showCloseButton: false,
              type: 'success',
              position: "top-center",
              timeout: 3000,
              toastBackgroundColor: '#4caf50'
            })
            this.loadTableItems()
          })
        this.close()
      } else {
        let date = new Date();
        this.editedItem.created_at = date.toLocaleDateString('ru-RU');
        API.post('add-order', this.editedItem)
          .then(response => {
            createToast(response.data.result, {
              showIcon: 'true',
              showCloseButton: false,
              type: 'success',
              position: "top-center",
              timeout: 3000,
              toastBackgroundColor: '#4caf50'
            })
            this.loadTableItems()
          })
      }
      this.close()
    },
  }
}
</script>

<style scoped>
.table {
  background: #fff;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
  font-size: 16px;
}
</style>
