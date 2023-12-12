<template>
  <v-app>

    <v-app-bar
      app
      color="primary"
      image=""
    >
      <v-app-bar-title>
        <h3 class="text-h4 white--text">{{ app_name }}</h3>
      </v-app-bar-title>
    </v-app-bar>

    <v-navigation-drawer
      image="https://img3.akspic.ru/crops/1/9/6/3/1/113691/113691-sinij_cvet-lazur-svet-geometricheskaya_forma-atmosfera-2048x1152.jpg"
      permanent="" expand-on-hover="" rail="">
      <v-list>
        <v-list-item
          base-color="white"
          prepend-avatar="/kompyuternyj-servis.png"
          :title="user.fullName"
          :subtitle="user.email"
        ></v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list density="compact" nav="">
        <v-list-item
          :to="links.profile"
          color="red"
          base-color="white"
          variant=""
          prepend-icon="mdi-account-circle-outline"
          :title="nav_menu.btn_lk"
          value="lk">
        </v-list-item>
        <v-list-item
          :to="links.services"
          color="red"
          base-color="white"
          variant=""
          prepend-icon="mdi-archive-outline"
          :title="nav_menu.btn_services"
          value="archive">
        </v-list-item>
        <v-list-item
          color="red"
          base-color="white"
          variant=""
          prepend-icon="mdi-card-plus-outline"
          :title="nav_menu.btn_add_client"
          value="new_serv">
        </v-list-item>
        <v-list-item
          color="red"
          base-color="white"
          variant=""
          prepend-icon="mdi-logout"
          :title="nav_menu.btn_logout"
          value="logout">
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view></router-view>
    </v-main>

  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    app_name: 'Сервисный центр',
    user: {
      fullName: 'Test Test',
      email: 'test@gmail.com'
    },
    nav_menu: {
      btn_lk: 'Личный кабинет',
      btn_services: 'Архив услуг',
      btn_add_client: 'Добавление клиента',
      btn_logout: 'Выход',
    },
    links: {
      main: '/',
      login: '/login',
      profile: '/profile',
      services: '/services',
    },
  }),
}
</script>
