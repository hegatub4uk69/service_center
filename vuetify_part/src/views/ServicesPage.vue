<template>
  <v-container style="height: 80px">
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
  <v-container>
    <v-row dense="">
      <v-col>
        <!--Таблица данных заказов-->
        <v-data-table
          v-model:expanded="expanded"
          :headers="ordersHeaders"
          :search="search"
          :items="filteredItems"
          :loading="loadingTable"
          :show-expand="true"
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
                max-width="500px"
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
                <v-card>
                  <v-card-title>
                    <span class="text-h5">{{ formTitle }}</span>
                  </v-card-title>
                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-text-field
                          v-model="editedItem.title"
                          label="Наименование техники"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="editedItem.category_id"
                          :items="categories"
                          item-title="name"
                          item-value="id"
                          label="Категория техники"
                          @update:menu="loadSelectCategory"
                        >
                        </v-select>
                      </v-row>
                      <!--Выпадающий список с выбором клиента-->
                      <v-row>
                        <v-autocomplete
                          v-model="editedItem.client_id"
                          :items="clients"
                          color="blue-grey-lighten-2"
                          item-title="phone"
                          item-value="id"
                          label="Клиент"
                          @update:menu="loadSelectClient"
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
                      color="blue-darken-1"
                      variant="text"
                      @click="save"
                    >
                      Оформить
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
              <!--Диалоговое окно удаления заказа-->
              <v-dialog v-model="dialogDelete" max-width="500px">
                <v-card>
                  <v-card-title class="text-h5">Вы уверены, что хотите удалить данную услугу?</v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Закрыть</v-btn>
                    <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">Удалить</v-btn>
                    <v-spacer></v-spacer>
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
          <!--Выпадающее описание заказа-->
          <template v-slot:expanded-row="{ columns, item }">
            <tr>
              <td :colspan="columns.length">
                <v-chip color="pink" label>Описание дефектов техники</v-chip>
                {{ item.description }}
              </td>
            </tr>
          </template>
          <!--Кнопки действий над заказами-->
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon
              size="small"
              color="purple"
              class="me-2"
              icon="mdi-account-circle-outline"
            >
            </v-icon>
            <v-icon
              size="small"
              class="me-2"
              color="info"
              icon="mdi-pencil-outline"
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
  <v-alert
    v-if="alert_success === true"
    type="success"
    title="zaebis"
    :text="alert"
  >
  </v-alert>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      dialog: false,
      dialogDelete: false,
      search: '',
      expanded: [],
      selected_status: 'Все',
      statuses: ['Все', 'Новый', 'В работе', 'Готов', 'Выдан', 'Отклонён'],
      ordersHeaders: [
        {title: '№', align: 'start', key: 'id'},
        {title: 'Наименование техники', key: 'title'},
        {title: 'Категория', key: 'categoryTitle'},
        {title: 'Клиент', key: 'client_FN'},
        {title: 'Приемщик', key: 'staff_in_FN'},
        {title: 'Техник', key: 'executor_FN'},
        {title: 'Статус', key: 'status', align: 'start'},
        {title: 'Действия', key: 'actions', sortable: false},
        {title: '', key: 'data-table-expand'},
      ],
      editedIndex: -1,
      editedItem: {
        title: '',
        category_id: null,
        status: 'Новый',
        client_id: null,
        staff_in_id: 1,
        executor_id: 1,
        description: '',
        created_at: null,
      },
      defaultItem: {
        title: '',
        category_id: null,
        status: 'Новый',
        client_id: null,
        staff_in_id: 1,
        executor_id: 1,
        description: '',
      },
      clients: [],
      selected_client: [],
      orders: [],
      categories: [],
      selected_category: [],
      loadingTable: true,
      alert: [],
      alert_success: false,
    }
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'Новый заказ' : 'Изменение заказа'
    },
    filteredItems() {
      if (this.selected_status === 'Все') {
        return this.orders
      } else {
        return this.orders.filter((i) => {
          return i.status === this.selected_status;
        })
      }
    },
  },

  watch: {
    dialog(val) {
      val || this.close()
    },
    dialogDelete(val) {
      val || this.closeDelete()
    },
  },

  methods: {
    loadSelectCategory() {
      axios.post('http://localhost:8000/get-categories')
        .then(response => {
          this.categories = response.data.result
        })
    },
    loadSelectClient() {
      axios.post('http://localhost:8000/get-clients')
        .then(response => {
          this.clients = response.data.result
        })
    },
    loadTableItems() {
      this.loadingTable = true
      axios.post('http://localhost:8000/get-orders')
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
    editItem(item) {
      this.editedIndex = this.orders.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem(item) {
      this.editedIndex = this.orders.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteItemConfirm() {
      this.orders.splice(this.editedIndex, 1)
      this.closeDelete()
    },
    close() {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    closeDelete() {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    save() {
      let date = new Date();
      this.editedItem.created_at = date.toLocaleDateString('ru-RU');
      axios.post('http://localhost:8000/add-order', this.editedItem)
        .then(response => {
          this.alert = response.data.result
          this.alert_success = true
        })
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
}

.radio-btn /deep/ label {
  color: #181818;
}

.table-title /deep/ label {
  color: #181818;
}
</style>
