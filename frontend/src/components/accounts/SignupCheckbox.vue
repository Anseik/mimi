<template>
<div style="width: 100%;">
  <v-col>
    <strong>서비스 약관에 동의해주세요</strong>
    <v-checkbox v-model="boxAll" @click="checkedAll">
      <template v-slot:label>
        <div style="font-size: 1.1rem; margin-left: 1rem;">
          <strong>모두 동의합니다.</strong>
        </div>
      </template>
    </v-checkbox>
    <v-card
      class="mx-auto"
      max-width="100%"
      outlined
    >
      <v-list-item>
        <v-list-item-content style="padding: 0;">
          <v-list-item-title class="headline mb-1">
              <v-container fluid style="padding: 0;">
                <v-checkbox v-for="(box, idx) in boxes" :key="idx" v-model="box.checkbox" @click="selected">
                  <template v-slot:label>
                    <div style="font-size: 1.1rem; margin-left: 1rem;">
                      {{box.text}}
                    </div>
                  </template>
                </v-checkbox>
              </v-container>
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-card>
  </v-col>

  <v-col cols="12">
    <v-btn style="background-color: #0275d8; color: white; 
      font-size: 1.3rem; font-weight: bold; 
      width: 100%; height: 3rem;"
      :disabled="!boxAll || !enable"
      @click="signup"
    >
      동의하고 가입하기
    </v-btn>
  </v-col>

</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'SignupCheckbox',
  data: () => ({
    boxAll: false,
    boxes: [
      {
        checkbox: false, text: '[필수] 만 14세 이상입니다'
      },
      {
        checkbox: false, text: '[필수] 미미여지도 이용약관 동의'
      },
      {
        checkbox: false, text: '[필수] 전자금융거래 이용약관 동의'
      },
      {
        checkbox: false, text: '[필수] 개인정보 수집 및 이용 동의'
      },
      {
        checkbox: false, text: '[필수] 개인정보 제공 동의'
      },
    ]
  }),
  props: {
    enable: Boolean,
    form: Object,
  },
  methods: {
    checkedAll() {
      for (let i in this.boxes) {
        this.boxes[i].checkbox = this.boxAll
      }
    },
    selected() {
      for (let i in this.boxes) {
        if(! this.boxes[i].checkbox) {
          this.boxAll = false;
          return
        } else {
          this.boxAll = true;
        }
      }
    },
    signup() {
      axios.post(`http://127.0.0.1:8000/mimi/member/sign-up`, this.form)
        .then(res => {
          console.log(res)
          alert('회원가입 성공')
          this.$router.push({name: 'Login'})
          // axios.post(``, {
          //   username: this.form.id,
          //   password: this.form.password,
          // }, {
          //   headers: {
          //     'mimi-authorization': "",
          //   }
          // })
          //   .then(response => {
          //     console.log(response)
          //     this.$router.push( {name: 'Login'} )
          //   })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
  .v-messages {
    display: none;
  }
</style>