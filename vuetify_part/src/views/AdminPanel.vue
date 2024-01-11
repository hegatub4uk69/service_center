<template>
  <v-container fluid="">
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4" lg="12">
        <v-card>
          <v-tabs
              v-model="tab"
              bg-color="primary"
              align-tabs="center"
          >
            <v-tab prepend-icon="mdi-account-box" value="tab-1">
              Сотрудники
            </v-tab>
            <v-tab prepend-icon="mdi-account-cash" value="tab-2">
              Клиенты
            </v-tab>
            <v-tab prepend-icon="mdi-book-cog-outline" value="tab-3">
              Заказы
            </v-tab>
            <v-tab prepend-icon="mdi-shape" value="tab-1">
              Категории техники
            </v-tab>
          </v-tabs>

          <v-window v-model="tab">
            <v-window-item style="transition: none" value="tab-1">
              <test2 v-if="tab === 'tab-1'"></test2>
            </v-window-item>
            <v-window-item style="transition: none" value="tab-2">
              <test3 v-if="tab === 'tab-2'"></test3>
            </v-window-item>
            <v-window-item style="transition: none" value="tab-3">
              <test2 v-if="tab === 'tab-1'"></test2>
            </v-window-item>
          </v-window>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Categories from "@/components/Categories.vue";
import Staff from "@/components/Clients.vue";

export default {
  name: 'AdminPanel',
  components: {
    'test2': Categories,
    'test3': Staff
  },
  data() {
    return {
      tab: 'tab-2',
    }
  },
}
</script>

<style>

</style>
