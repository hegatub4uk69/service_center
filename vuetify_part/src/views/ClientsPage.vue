<template>
  <v-container>
    <v-row justify="center" dense="">
      <v-col lg="4">
        <v-card>
          <v-data-iterator
            :items="tests"
            :items-per-page="5"
            :search="search"
          >
            <template v-slot:header>
              <v-toolbar>
                <v-toolbar-title style="font-size: 25px">
                  <v-icon class="mb-1 mr-1" icon="mdi-account-group-outline"></v-icon>
                  Клиенты
                </v-toolbar-title>
                <v-spacer></v-spacer>
                <v-text-field
                  class="px-2"
                  v-model="search"
                  clearable
                  density="comfortable"
                  hide-details
                  placeholder="Поиск"
                  prepend-inner-icon="mdi-magnify"
                  style="max-width: 300px;"
                  variant="solo"
                ></v-text-field>
              </v-toolbar>
            </template>

            <template v-slot:default="{ items }">
              <v-container class="pa-2" fluid>
                <v-list
                  lines="two"
                  density="compact"
                  nav
                >
                  <v-list-item
                    v-for="(item, i) in items"
                    :key="i"
                    :value="item"
                    :title="item?.raw?.title"
                    :subtitle="item?.raw?.subtitle"
                    color="primary"
                  >
                    <template v-slot:prepend>
                      <v-icon
                        style="font-size: 40px"
                        icon="mdi-account-circle-outline">
                      </v-icon>
                    </template>
                    <template v-slot:title>
                      <v-list-item-title style="font-size: 18px">{{ item?.raw?.title }}</v-list-item-title>
                    </template>
                    <template v-slot:subtitle>
                      <v-list-item-subtitle style="font-size: 15px;">{{ item?.raw?.subtitle }}</v-list-item-subtitle>
                    </template>
                  </v-list-item>
                </v-list>
              </v-container>
            </template>

            <template v-slot:footer="{ page, pageCount, prevPage, nextPage }">
              <div class="d-flex align-center justify-center pa-4">
                <v-btn
                  :disabled="page === 1"
                  icon="mdi-arrow-left"
                  density="comfortable"
                  variant="tonal"
                  rounded
                  @click="prevPage"
                ></v-btn>

                <div class="mx-2 text-caption">
                  <span style="font-size: 15px">Страница {{ page }} из {{ pageCount }}</span>
                </div>

                <v-btn
                  :disabled="page >= pageCount"
                  icon="mdi-arrow-right"
                  density="comfortable"
                  variant="tonal"
                  rounded
                  @click="nextPage"
                ></v-btn>
              </div>
            </template>
          </v-data-iterator>
        </v-card>
      </v-col>
      <v-col lg="4">
        <v-card>
          <v-card-text>
            <v-text-field></v-text-field>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      search: '',
      tests: [
        {
          prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          title: 'Королёв Евгений Геннадьевич',
          subtitle: `+79459334436`,
        },
        {
          prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          title: 'Summer BBQ',
          subtitle: `Wish I could come, but I'm out of town this weekend.`,
        },
        {
          prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          title: 'Oui oui',
          subtitle: 'Do you have Paris recommendations? Have you ever been?',
        },
        {
          prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
          title: 'Birthday gift',
          subtitle: 'Have any ideas about what we should get Heidi for her birthday?',
        },
        {
          prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
          title: 'Recipe to try',
          subtitle: 'We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
        },
      ],
      games: [
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/4.png',
          title: 'The Sci-Fi Shooter Experience',
          subtitle: 'Dive into a futuristic world of intense battles and alien encounters.',
          advanced: false,
          duration: '8 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/2.png',
          title: 'Epic Adventures in Open Worlds',
          subtitle: 'Embark on a journey through vast, immersive landscapes and quests.',
          advanced: true,
          duration: '10 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/3.png',
          title: 'Surviving the Space Station Horror',
          subtitle: 'Navigate a haunted space station in this chilling survival horror game.',
          advanced: false,
          duration: '9 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/5.png',
          title: 'Neon-Lit High-Speed Racing Thrills',
          subtitle: 'Experience adrenaline-pumping races in a futuristic, neon-soaked city.',
          advanced: true,
          duration: '12 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/6.png',
          title: 'Retro-Style Platformer Adventures',
          subtitle: 'Jump and dash through pixelated worlds in this classic-style platformer.',
          advanced: false,
          duration: '11 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/7.png',
          title: 'Medieval Strategic War Campaigns',
          subtitle: 'Lead armies into epic battles and conquer kingdoms in this strategic game.',
          advanced: true,
          duration: '10 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/1.png',
          title: 'Underwater VR Exploration Adventure',
          subtitle: 'Dive deep into the ocean and discover the mysteries of the underwater world.',
          advanced: true,
          duration: '11 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/8.png',
          title: '1920s Mystery Detective Chronicles',
          subtitle: 'Solve crimes and uncover secrets in the glamourous 1920s era.',
          advanced: false,
          duration: '9 minutes',
        },
      ],
    }
  },
  methods: {
    onClickSeeAll() {
      this.itemsPerPage = this.itemsPerPage === 4 ? this.mice.length : 4
    },
  },
}
</script>

<style>

</style>
