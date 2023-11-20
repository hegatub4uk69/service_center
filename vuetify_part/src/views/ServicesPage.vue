<template>
  <v-container style="height: 80px">
    <v-card style="height: 70px" color="">
      <v-row align="center" justify="center" dense="">
        <v-col cols="4" sm="4" md="4" lg="3">
          <!--Кнопки фильтрации данных в таблице-->
          <v-select label="Фильтрация по статусу"></v-select>
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
          >
          </v-text-field>
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
            :headers="servicesHeaders"
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
                            v-model="editedItem.name"
                            label="Наименование техники"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select label="Категория техники"></v-select>
                      </v-row>
                      <!--Выпадающий список с выбором клиента-->
                      <v-row>
                        <v-autocomplete
                            v-model="friends"
                            :items="people"
                            :chips="true"
                            closable-chips
                            color="blue-grey-lighten-2"
                            item-title="name"
                            item-value="id"
                            label="Клиент"
                            :multiple="true"
                        >
                          <template v-slot:chip="{ props, item }">
                            <v-chip
                                v-bind="props"
                                :prepend-icon="item.raw.avatar"
                                :text="item.raw.name + ' ' + item.raw.group"
                            ></v-chip>
                          </template>
                          <template v-slot:item="{ props, item }">
                            <v-list-item
                                v-bind="props"
                                :disabled="this.friends.length >= 1"
                                :prepend-icon="item?.raw?.avatar"
                                :title="item?.raw?.name"
                                :subtitle="item?.raw?.group"
                            ></v-list-item>
                          </template>
                        </v-autocomplete>
                      </v-row>
                      <v-row>
                        <v-textarea label="Описание"></v-textarea>
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
</template>

<script>
import axios from "axios";

export default {
  data() {
    const srcs = {
      1: 'mdi-account-circle-outline',
    }
    return {
      sortBy: 'id',
      dialog: false,
      dialogDelete: false,
      search: '',
      radios: 'all',
      expanded: [],
      friends: [],
      people: [
        // { header: 'Group 1' },
        {id: 1, name: 'Sandra Adams Father_name', group: 'Group 1', avatar: srcs[1]},
        {id: 2, name: 'Ali Connors Father_name', group: 'Group 1', avatar: srcs[1]},
        {id: 3, name: 'Trevor Hansen Father_name', group: 'Group 1', avatar: srcs[1]},
        {id: 4, name: 'Tucker Smith Father_name', group: 'Group 1', avatar: srcs[1]},
        // { divider: true },
        // { header: 'Group 2' },
        {name: 'Britta Holt Father_name', group: 'Group 2', avatar: srcs[1]},
        {name: 'Jane Smith Father_name', group: 'Group 2', avatar: srcs[1]},
        {name: 'John Smith Father_name', group: 'Group 2', avatar: srcs[1]},
        {name: 'Sandra Williams Father_name', group: 'Group 2', avatar: srcs[1]},
      ],
      statuses: {
        all_status: true,
        new_status: false,
        work_status: false,
        done_status: false,
        wait_text: 'Новый',
        work_text: 'В работе',
        done_text: 'Готов',
      },
      servicesHeaders: [
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
        id: 0,
        name: '',
        category: '',
        status: 'Новый',
        staff: 'Test Test Test',
      },
      defaultItem: {
        name: '',
        category: '',
        status: 'Новый',
      },
      services: [],
      loadingTable: true,
    }
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'Новый заказ' : 'Изменение заказа'
    },
    filteredItems() {
      if (this.statuses.new_status === true && this.radios === 'new') {
        return this.services.filter((i) => {
          return i.status === this.statuses.wait_text;
        })
      } else if (this.statuses.work_status === true && this.radios === 'work') {
        return this.services.filter((i) => {
          return i.status === this.statuses.work_text;
        })
      } else if (this.statuses.done_status === true && this.radios === 'done') {
        return this.services.filter((i) => {
          return i.status === this.statuses.done_text;
        })
      } else if (this.statuses.all_status === true && this.radios === 'all') {
        return this.services
      }
      return []
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
    loadTableItems() {
      this.loadingTable = true
      axios.post('http://localhost:8000/get-orders')
          .then(response => {
            this.services = response.data.result
            this.loadingTable = false
          })
    },
    getAllData() {
      this.statuses.all_status = true
      this.statuses.new_status = false
      this.statuses.work_status = false
      this.statuses.done_status = false
    },
    getNewData() {
      this.statuses.all_status = false
      this.statuses.new_status = true
      this.statuses.work_status = false
      this.statuses.done_status = false
    },
    getWorkData() {
      this.statuses.all_status = false
      this.statuses.new_status = false
      this.statuses.work_status = true
      this.statuses.done_status = false
    },
    getDoneData() {
      this.statuses.all_status = false
      this.statuses.new_status = false
      this.statuses.work_status = false
      this.statuses.done_status = true
    },
    getColor(status) {
      if (status === 'Новый') return 'info'
      else if (status === 'В работе') return 'orange'
      else if (status === 'Готов') return 'green'
      else if (status === 'Выдан') return 'purple'
      else return 'red'
    },
    editItem(item) {
      this.editedIndex = this.services.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem(item) {
      this.editedIndex = this.services.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteItemConfirm() {
      this.services.splice(this.editedIndex, 1)
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
      if (this.editedIndex > -1) {
        Object.assign(this.services[this.editedIndex], this.editedItem)
      } else {
        this.services.push(this.editedItem)
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
}

.radio-btn /deep/ label {
  color: #181818;
}

.table-title /deep/ label {
  color: #181818;
}
</style>
