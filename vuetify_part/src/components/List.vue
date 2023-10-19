<template>
  <v-container>

    <v-row class="list__cafes-title">
      <v-col>
        <h2 class="text-center text-h3 py-3">Список оформленных услуг</h2>
        <v-divider color="black"></v-divider>
      </v-col>
    </v-row>

    <v-row dense="">
      <v-col
        cols="12" sm="8" md="4" lg="4"
        v-for="item in items_list"
        :key="item.id">
        <v-card class="h-100">
          <v-card-actions>
            <v-chip label="">{{ item.id }}</v-chip>
            <v-spacer></v-spacer>
            <v-chip class="ma-2" color="pink" label="" text-color="white">
              <v-icon start="" icon="mdi-label"></v-icon>
              {{ item.status }}
            </v-chip>
          </v-card-actions>
          <v-divider color="black"></v-divider>
          <v-card-actions>
            <v-icon icon="mdi-account-outline"></v-icon>
            <v-card-text>
              <p class="text-body-1">Сотрудник: {{ item.staff }}</p>
            </v-card-text>
          </v-card-actions>
          <v-card-actions>
            <v-card-text>
              <p class="text-body-1">Техника: {{ item.name }}</p>
            </v-card-text>
          </v-card-actions>
          <v-card-actions>
            <v-icon icon="mdi-devices"></v-icon>
            <v-card-text>
              <p class="text-body-1">Категория: {{ item.category }}</p>
            </v-card-text>
          </v-card-actions>
          <v-divider color="black"></v-divider>
          <v-card-actions>
            <v-btn
              color="orange-lighten-2" variant="text">Explore</v-btn>
            <v-spacer></v-spacer>
            <v-btn
              :icon="item.show ? 'mdi-chevron-up' : 'mdi-chevron-down'"
              @click="item.show = !item.show"
            ></v-btn>
          </v-card-actions>
          <v-expand-transition v-show="item.show">
            <div>
              <v-divider></v-divider>
              <v-card-text>{{ item.description }}</v-card-text>
            </div>
          </v-expand-transition>
        </v-card>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'List',
  data: () => ({
    show: false,
    items_list: [
      {
        id: 0,
        status: 'Ожидание',
        staff: 'Test Test Test',
        name: 'gt 710',
        category: 'Видеокарты',
        description: 'Не заполнено',
        show: false
      },
      {
        id: 1,
        status: 'Ожидание',
        staff: 'Test Test Test',
        name: 'r5 3600',
        category: 'Процессор',
        description: 'Не заполнено',
        show: false
      },
      {
        id: 2,
        status: 'Ожидание',
        staff: 'Test Test Test',
        name: 'r5 3600',
        category: 'Процессор',
        description: 'Не заполнено',
        show: false
      },
    ]
  })
}
</script>
