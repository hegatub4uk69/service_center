<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col lg="10">
        <v-card>
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
                @click="dialog_add_category = true"
            >Добавить
            </v-btn>
            <v-dialog v-model="dialog_add_category" width="525px">
              <v-card>
                <v-toolbar>
                  <v-toolbar-title style="font-size: 25px">
                    <v-icon class="mb-1 mr-1" icon="mdi-plus-box-outline"></v-icon>
                    Добавление категории техники
                  </v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <v-text-field
                      v-model="categoryData.name"
                      label="Наименование"
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
                      @click="dialog_add_category = false"
                  >
                    Закрыть
                  </v-btn>
                  <v-btn
                      style="margin-bottom: 4px"
                      density="default"
                      color="blue-darken-1"
                      variant="outlined"
                      @click="addCategory"
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
              :items="categories"
              :search="search"
              :items-per-page="5"
              item-value="id"
              class="elevation-1 table"
              @update:options="loadCategories"
          >
            <template v-slot:[`item.name`]="{item}">
              <v-text-field
                  v-model="item.name"
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
                  @click="editCategory(item)"
              >
              </v-icon>
              <v-icon
                  size="small"
                  color="red"
                  icon="mdi-delete-outline"
                  @click="deleteCategory(item)"
              >
              </v-icon>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {createToast} from "mosha-vue-toastify";
import 'mosha-vue-toastify/dist/style.css';
import API from "@/axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Categories',
  data() {
    return {
      search: '',
      categories: [],
      headers: [
        {title: 'ID', key: 'id', width: 50},
        {title: 'Наименование', key: 'name'},
        {title: 'Действия', key: 'actions', align: 'center', sortable: false, width: 120}
      ],
      dialog_add_category: false,
      categoryData: {
        name: null
      }
    }
  },
  methods: {
    loadCategories() {
      API.post('get-categories').then(response => {
        this.categories = response.data.result
      })
    },
    addCategory() {
      API.post('add-category', this.categoryData).then(response => {
        createToast(response.data.result, {
          showIcon: 'true',
          showCloseButton: false,
          type: 'success',
          position: "top-center",
          timeout: 3000,
          toastBackgroundColor: '#4caf50'
        })
        this.dialog_add_category = false
        this.loadCategories()
      })
    },
    editCategory(item) {
      API.post('update-category', {id: item.id, name: item.name}).then(response => {
        createToast(response.data.result, {
          showIcon: 'true',
          showCloseButton: false,
          type: 'success',
          position: "top-center",
          timeout: 3000,
          toastBackgroundColor: '#4caf50'
        })
        this.loadCategories()
      })
    },
    deleteCategory(item) {
      API.post('delete-category', {id: item.id}).then(response => {
        createToast(response.data.result, {
          showIcon: 'true',
          showCloseButton: false,
          type: 'success',
          position: "top-center",
          timeout: 3000,
          toastBackgroundColor: '#4caf50'
        })
        this.loadCategories()
      })
    }
  }
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
