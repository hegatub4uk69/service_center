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
            <v-tab prepend-icon="mdi-account-box" value="tab-staff">
              Сотрудники
            </v-tab>
<!--            <v-tab prepend-icon="mdi-account-settings-outline" value="tab-accounts">
              Аккаунты
            </v-tab>-->
            <v-tab prepend-icon="mdi-account-cash" value="tab-clients">
              Клиенты
            </v-tab>
            <v-tab prepend-icon="mdi-book-cog-outline" value="tab-orders">
              Заказы
            </v-tab>
            <v-tab prepend-icon="mdi-shape" value="tab-categories">
              Категории техники
            </v-tab>
          </v-tabs>

          <v-window v-model="tab">
            <v-window-item style="transition: none" value="tab-staff">
              <Staff v-if="tab === 'tab-staff'"></Staff>
            </v-window-item>
<!--            <v-window-item style="transition: none" value="tab-accounts">
              <Accounts v-if="tab === 'tab-accounts'"></Accounts>
            </v-window-item>-->
            <v-window-item style="transition: none" value="tab-clients">
              <Clients v-if="tab === 'tab-clients'"></Clients>
            </v-window-item>
            <v-window-item style="transition: none" value="tab-orders">
              <Orders v-if="tab === 'tab-orders'"></Orders>
            </v-window-item>
            <v-window-item style="transition: none" value="tab-categories">
              <Categories v-if="tab === 'tab-categories'"></Categories>
            </v-window-item>
          </v-window>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Categories from "@/components/Categories.vue";
import Staff from "@/components/Staff.vue";
import Clients from "@/components/Clients.vue";
import Orders from "@/components/Orders.vue";
// import Accounts from "@/components/Accounts.vue";

export default {
  name: 'AdminPanel',
  components: {
    'Categories': Categories,
    'Staff': Staff,
    'Clients': Clients,
    'Orders': Orders,
    // 'Accounts': Accounts
  },
  data() {
    return {
      tab: 'tab-staff',
    }
  },
}
</script>

<style>

</style>
