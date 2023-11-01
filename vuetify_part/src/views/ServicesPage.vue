<template>
  <v-container style="height: 80px">
    <v-card style="height: 70px" color="">
      <v-row align="center" justify="center" dense="">
        <v-col cols="12" sm="8" md="6" lg="5">
          <v-radio-group v-model="radios" inline>
            <v-spacer></v-spacer>
            <v-radio @click="getAllData"
                     class="radio-btn" label="Все" color="red" value="all"></v-radio>
            <v-spacer></v-spacer>
            <v-radio @click="getWaitData"
                     class="radio-btn" label="Ожидание" color="red" value="wait"></v-radio>
            <v-spacer></v-spacer>
            <v-radio @click="getWorkData"
                     class="radio-btn" label="В_работе" color="red" value="work"></v-radio>
            <v-spacer></v-spacer>
            <v-radio @click="getDoneData"
                     class="radio-btn" label="Готов" color="red" value="done"></v-radio>
            <v-spacer></v-spacer>
          </v-radio-group>
        </v-col>
        <v-col cols="12" sm="8" md="4" lg="5">
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
  <!--  <v-card
        class="text-center"
        position="absolute"
        color="success"
        style="z-index: 999; top: 126px; left: 113px; height: 80px; width: 80px">
      <v-icon color="" class="my-5" size="40px" icon="mdi-book"></v-icon>
    </v-card>-->
  <v-container>
    <v-row dense="">
      <v-col>
        <v-data-table
          v-model:expanded="expanded"
          :headers="servicesHeaders"
          :search="search"
          :items="filteredItems"
          item-value="id"
          show-expand=""
          class="elevation-1 table"
        >
          <template v-slot:top>
            <v-toolbar flat="" color="white">
              <v-toolbar-title style="font-size: 25px">
                <v-icon class="mb-1"
                        icon="mdi-book-open-outline"
                ></v-icon> Заказы
              </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-dialog
                v-model="dialog"
                max-width="500px"
              >
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
          <template v-slot:[`item.status`]="{ value }">
            <v-chip :color="getColor(value)">
              {{ value }}
            </v-chip>
          </template>
          <template v-slot:expanded-row="{ columns, item }">
            <tr>
              <td :colspan="columns.length">
                Описание дефектов {{ item.name }}:
                {{ item.description }}
              </td>
            </tr>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
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
export default {
  data() {
    return {
      dialog: false,
      dialogDelete: false,
      search: '',
      radios: 'all',
      expanded: [],
      statuses: {
        all_status: true,
        wait_status: false,
        work_status: false,
        done_status: false,
        wait_text: 'Ожидание',
        work_text: 'В работе',
        done_text: 'Готов',
      },
      servicesHeaders: [
        {
          title: 'Номер',
          align: 'start',
          sortable: false,
          key: 'id',
        },
        {title: 'Наименование', key: 'name'},
        {title: 'Категория', key: 'category'},
        {title: 'Сотрудник', key: 'staff'},
        {title: 'Статус', key: 'status', align: 'start'},
        {title: 'Действия', key: 'actions', sortable: false},
        {title: '', key: 'data-table-expand'},
      ],
      editedIndex: -1,
      editedItem: {
        id: 0,
        name: '',
        category: '',
        status: 'Ожидание',
        staff: 'Test Test Test',
      },
      defaultItem: {
        name: '',
        category: '',
        status: 'Ожидание',
      },
      services: [
        {
          id: 0,
          status: 'Ожидание',
          staff: 'Test Test Test',
          name: 'gt 710',
          category: 'Видеокарты',
          description: 'Кулеры крутятся, а изображения нет',
        },
        {
          id: 1,
          status: 'В работе',
          staff: 'Test Test Test',
          name: 'gt 1030',
          category: 'Видеокарты',
          description: 'Нет изображения',
        },
        {
          id: 2,
          status: 'Готов',
          staff: 'Test Test Test',
          name: 'r5 3600',
          category: 'Процессоры',
          description: 'Не заполнено',
        },
        {
          id: 3,
          status: 'Ожидание',
          staff: 'Test Test Test',
          name: 'gt 710',
          category: 'Видеокарты',
          description: 'Не заполнено',
        },
        {
          id: 4,
          status: 'Ожидание',
          staff: 'Test Test Test',
          name: 'test',
          category: 'Видеокарты',
          description: 'Не заполнено',
        },
        {
          id: 5,
          status: 'Ожидание',
          staff: 'Test Test Test',
          name: 'test',
          category: 'Видеокарты',
          description: 'Не заполнено',
        },
        {
          id: 6,
          status: 'Ожидание',
          staff: 'Test Test Test',
          name: 'test',
          category: 'Видеокарты',
          description: 'Не заполнено',
        },
        {
          id: 7,
          status: 'Ожидание',
          staff: 'Test Test Test',
          name: 'test',
          category: 'Видеокарты',
          description: 'Не заполнено',
        },
        {
          id: 8,
          status: 'Ожидание',
          staff: 'Test Test Test',
          name: 'test',
          category: 'Видеокарты',
          description: 'Не заполнено',
        },
        {
          id: 9,
          status: 'Ожидание',
          staff: 'Test Test Test',
          name: 'test',
          category: 'Видеокарты',
          description: 'Не заполнено',
        },
      ],
    }
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'Новый заказ' : 'Изменение заказа'
    },
    filteredItems() {
      if (this.statuses.wait_status === true && this.radios === 'wait') {
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
    getAllData() {
      this.statuses.all_status = true
      this.statuses.wait_status = false
      this.statuses.work_status = false
      this.statuses.done_status = false
    },
    getWaitData() {
      this.statuses.all_status = false
      this.statuses.wait_status = true
      this.statuses.work_status = false
      this.statuses.done_status = false
    },
    getWorkData() {
      this.statuses.all_status = false
      this.statuses.wait_status = false
      this.statuses.work_status = true
      this.statuses.done_status = false
    },
    getDoneData() {
      this.statuses.all_status = false
      this.statuses.wait_status = false
      this.statuses.work_status = false
      this.statuses.done_status = true
    },
    getColor(status) {
      if (status === 'Ожидание') return 'info'
      else if (status === 'В работе') return 'orange'
      else return 'green'
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
