<template>
  <v-row class="fill-height">
    <v-col>
      <v-sheet height="">
        <v-toolbar
          flat
        >
          <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="setToday"
          >
            Today
          </v-btn>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="prev"
          >
            <v-icon small>
              mdi-chevron-left
            </v-icon>
          </v-btn>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="next"
          >
            <v-icon small>
              mdi-chevron-right
            </v-icon>
          </v-btn>
          <v-toolbar-title v-if="$refs.calendar">
            {{ $refs.calendar.title }}
          </v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
      </v-sheet>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          :events="events"
          :event-color="getEventColor"
          :type="type"
          @click:event="showEvent"
        ></v-calendar>
        <v-menu
          v-model="selectedOpen"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
          <v-card
            color="grey lighten-4"
            
            flat
          >
            <v-toolbar
              :color="selectedEvent.color"
              dark
            >
              <v-toolbar-title v-html="selectedEvent.storeName" @click="moveStoreDetail"></v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon v-if="selectedEvent.visit==false" @click="selectedEvent.visit=true">
                <v-icon>mdi-map-marker-check-outline</v-icon>
              </v-btn>
              <v-btn icon v-if="selectedEvent.visit==true" @click="selectedEvent.visit=false">
                <v-icon>mdi-map-marker-check</v-icon>
              </v-btn>
            </v-toolbar>
            <v-card-text>
              <span v-html="selectedEvent.details"></span>
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="secondary"
                @click="selectedOpen = false"
              >
                Cancel
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-sheet>
      <div>
        <h4 class="ml-3 mt-3">{{ this.focus }} 일정</h4>
        <v-row class="mt-1 mx-1">
          <v-col cols=4 class="">
            <p class="text-center">아침</p>
            <v-card
              class=""
              max-height=""
            >
              <template slot="progress">
                <v-progress-linear
                  color="deep-purple"
                  height="10"
                  indeterminate
                ></v-progress-linear>
              </template>

              <v-img
                height=""
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
              ></v-img>

              <v-card-title class="pa-0">식당명</v-card-title>

              <v-card-text class="pa-3">
                <v-row
                  align=""
                  class=""
                >
                  <v-rating
                    :value="4.5"
                    color="amber"
                    dense
                    half-increments
                    readonly
                    size="14"
                  ></v-rating>

                  <div class="grey--text">
                    4.5 (413)
                  </div>
                </v-row>
              </v-card-text>
            </v-card>     
          </v-col>
          <v-col cols=4 class="">
            <p class="text-center">점심</p>
            <v-card
              class=""
              max-height=""
            >
              <template slot="progress">
                <v-progress-linear
                  color="deep-purple"
                  height="10"
                  indeterminate
                ></v-progress-linear>
              </template>

              <v-img
                height=""
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
              ></v-img>

              <v-card-title class="pa-0">식당명</v-card-title>

              <v-card-text class="pa-3">
                <v-row
                  align=""
                  class=""
                >
                  <v-rating
                    :value="4.5"
                    color="amber"
                    dense
                    half-increments
                    readonly
                    size="14"
                  ></v-rating>

                  <div class="grey--text">
                    4.5 (413)
                  </div>
                </v-row>
              </v-card-text>
            </v-card>           
          </v-col>
          <v-col cols=4 class="">
            <p class="text-center">저녁</p>
            <v-card
              class=""
              max-height=""
            >
              <template slot="progress">
                <v-progress-linear
                  color="deep-purple"
                  height="10"
                  indeterminate
                ></v-progress-linear>
              </template>

              <v-img
                height=""
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
              ></v-img>

              <v-card-title class="pa-0">식당명</v-card-title>

              <v-card-text class="pa-3">
                <v-row
                  align=""
                  class=""
                >
                  <v-rating
                    :value="4.5"
                    color="amber"
                    dense
                    half-increments
                    readonly
                    size="14"
                  ></v-rating>

                  <div class="grey--text">
                    4.5 (413)
                  </div>
                </v-row>
              </v-card-text>
            </v-card>             
          </v-col>
        </v-row>
      </div>
    </v-col>
  </v-row>
</template>

<script>
import axios from 'axios'
export default {
  name : "Diary",
  components: {
    
  },
  data: () => ({
    focus: '',
    type: 'month',
    selectedEvent: {},
    selectedElement: null,
    selectedOpen: false,
    events: [
      {
        name: '아침', 
        storeId: 1, 
        storeName: '국수이야기', 
        image: '', 
        start: new Date(2021, 2, 27, 9), 
        end: new Date(2021, 2, 27, 10), 
        color: 'blue', 
        visit: false,
        details: '가게 정보',
      },
      {
        name: '점심', 
        storeId: 2, 
        storeName: '라면이야기', 
        image: '', 
        start: new Date(2021, 2, 27, 12), 
        end: new Date(2021, 2, 27, 13), 
        color: 'deep-purple', 
        visit: false,
        details: '가게 정보',
      },
      {
        name: '저녁', 
        storeId: 3, 
        storeName: '우동이야기', 
        image: '', 
        start: new Date(2021, 2, 27, 18), 
        end: new Date(2021, 2, 27, 19), 
        color: 'cyan', 
        visit: false,
        details: '가게 정보',
      },
      {
        name: '저녁', 
        storeId: 1, 
        storeName: '돈까스맛집', 
        image: '', 
        start: new Date(2021, 2, 28, 18), 
        end: new Date(2021, 2, 28, 19), 
        color: 'cyan', 
        visit: false,
        details: '가게 정보',
      },
      {
        name: '점심', 
        storeId: 1, 
        storeName: '초밥집', 
        image: '', 
        start: new Date(2021, 2, 26, 18), 
        end: new Date(2021, 2, 26, 19), 
        color: 'blue',
        visit: false,
        details: '가게 정보',
      },
    ],
    colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
  }),
  methods: {
    setToday () {
      let today = new Date()
      let todayString = ''
      let year = today.getFullYear()
      let month = today.getMonth() + 1
      if (month < 10) {
        month = "0".concat(month)
      }
      let date = today.getDate()
      if (date < 10) {
        date = "0".concat(date)
      }
      this.focus = todayString.concat(year, "-", month, "-", date)      
    },
    prev () {
      this.$refs.calendar.prev()
    },
    next () {
      this.$refs.calendar.next()
    },
    getEvents() {
      // 저장된 이벤트 받아오기
      axios.get('')
    },
    getEventColor (event) {
      return event.color
    },
    showEvent ({ nativeEvent, event }) {
      const open = () => {
        this.selectedEvent = event
        this.selectedElement = nativeEvent.target
        setTimeout(() => {
          this.selectedOpen = true
        }, 10)
      }

      if (this.selectedOpen) {
        this.selectedOpen = false
        setTimeout(open, 10)
      } else {
        open()
      }

      nativeEvent.stopPropagation()
    },
    moveStoreDetail() {
      console.log('가게 상세조회 화면으로 이동')
    }
  },
  mounted () {
    this.$refs.calendar.checkChange()
  },
  created() {
    this.setToday()
  }
}
</script>

<style>

</style>