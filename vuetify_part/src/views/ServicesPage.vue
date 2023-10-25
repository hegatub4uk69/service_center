<template>
  <v-container>
    <v-row dense="">
      <v-col>
        <v-data-table
          v-model:expanded="expanded"
          :headers="servicesHeaders"
          :items="services"
          item-value="id"
          show-expand=""
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar flat="">
              <v-toolbar-title>
                <v-icon icon="mdi-book-outline"></v-icon>
                Таблица оформленных услуг
              </v-toolbar-title>
              <v-divider
                class="mx-4"
                inset=""
                vertical=""
              ></v-divider>
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
                  >
                    Новая услуга
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title>
                    <span class="text-h5">{{ formTitle }}</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col
                          cols="12"
                          sm="6"
                          md="4"
                        >
                          <v-text-field
                            v-model="editedItem.name"
                            label="Наименование"
                          ></v-text-field>
                        </v-col>
                        <v-col
                          cols="12"
                          sm="6"
                          md="4"
                        >
                          <v-text-field
                            v-model="editedItem.category"
                            label="Категория"
                          ></v-text-field>
                        </v-col>
                        <v-col
                          cols="12"
                          sm="6"
                          md="4"
                        >
                          <v-text-field
                            v-model="editedItem.status"
                            label="Статус"
                          ></v-text-field>
                        </v-col>
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
                      Сохранить
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
            <tr bgcolor="black">
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
      expanded: [],
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
          status: 'Исполнен',
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
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
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
      this.desserts.splice(this.editedIndex, 1)
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
/*.table-header {
  background-color: #ce6666;
}*/
</style>
