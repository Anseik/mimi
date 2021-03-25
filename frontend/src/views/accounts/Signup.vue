<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col
          cols="12"
          class="pb-0"
        >
          <strong>회원정보를 입력해주세요</strong>
          
          <!-- email -->
          <v-text-field
            style="margin-top: 1rem;"
            solo
            flat
            dense
            outlined
            prepend-inner-icon="mdi-email-outline"
            :rules="[required_id, emailRules,]"
            label="아이디(이메일)"
            v-model="form.email"
          ></v-text-field>

          <!-- email중복 확인, 인증번호 발송 -->
          <!-- 중복이면 이미 가입된 이메일이라는 팝업 -->
          <!-- 가입되지 않은 이메일이면 인증번호 발송 -->
          <v-btn 
            block
            @click="sendCertNum"
            class="mb-5"
          >이메일 중복 확인 / 인증번호 발송</v-btn>

          <!-- 인증번호 입력 -->
          <v-row v-if="showCert">
            <v-col cols=8>
              <v-text-field
                solo
                flat
                dense
                outlined
                prepend-inner-icon="mdi-key"
                label="인증번호"
              ></v-text-field>
            </v-col>
            <v-col cols=4 class="mt-1">
              <v-btn block large>확인</v-btn>
            </v-col>
          </v-row>
          
          <!-- 비밀번호 입력 -->
          <v-text-field
            v-model="form.pw"
            solo
            flat
            dense
            outlined
            required
            prepend-inner-icon="mdi-lock-outline"
            :rules="[required, min_pw]"
            type="password"
            label="비밀번호"
          ></v-text-field> 

          <!-- 비밀번호 확인 -->
          <v-text-field
            solo
            flat
            dense
            outlined
            required
            prepend-inner-icon="mdi-lock-check-outline"
            :rules="[passwordConfirmationRule]"
            v-model="rePassword"
            type="password"
            label="비밀번호 확인"
          ></v-text-field>

          <!-- 성별 -->
          <v-row class="">
            <v-col cols="2" class="pr-0 pb-0">
              <div class="mt-1">성별</div>
            </v-col>
            <v-col cols="10" class="pl-0 pb-0">
              <v-radio-group
                v-model="form.gender"
                row
                class="mt-0"
              >
                <v-radio
                  label="남성"
                  value="0"
                ></v-radio>
                <v-radio
                  label="여성"
                  value="1"
                ></v-radio>
              </v-radio-group>
            </v-col>
          </v-row>

          <!-- 생년월일 -->
          <v-menu
            ref="menu"
            v-model="menu"
            :close-on-content-click="false"
            :return-value.sync="form.date"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="form.date"
                label="생년월일"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="form.date"
              no-title
              scrollable
            >
              <v-spacer></v-spacer>
              <v-btn
                text
                color="primary"
                @click="menu = false"
              >
                Cancel
              </v-btn>
              <v-btn
                text
                color="primary"
                @click="$refs.menu.save(form.date)"
              >
                OK
              </v-btn>
            </v-date-picker>
          </v-menu>          
        </v-col>

        <v-col cols="12">
          <v-divider></v-divider>
        </v-col>
        
        <!-- 약관 동의 -->
        <SignupCheckbox :form="form" :enable="enable" />

        <!-- 푸터 -->
        <v-col>
          <AccountsFooter />
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import SignupCheckbox from '../../components/accounts/SignupCheckbox.vue'
import AccountsFooter from '../../components/accounts/AccountsFooter.vue'
import axios from 'axios'

export default {
  components: { AccountsFooter, SignupCheckbox },
  name: 'Signup',
  data: () => ({
    rePassword: '',
    form: {
      email: '',
      pw: '',
      gender: '',
      date: '',
    },
    showCert: false,
    menu: false,
  }),
  methods: {
    action() {
      console.log(this.form)
    },
    sendCertNum() {
      console.log('인증번호 발송')
      this.showCert = true
      axios.get(`http://127.0.0.1:8000/mimi/member/auth-email/${this.form.email}`)
    }
  },
  computed: {
    required() {
      return () => !!this.form.pw || '비밀번호를 입력해주세요.'
    },
    required_id() {
      return () => !!this.form.email || '아이디(이메일)를 입력해주세요.'
    },
    min_pw() {
      return () => this.form.pw.length >= 8 || '비밀번호를 8자 이상 작성해주세요.'
    },
    emailRules() {
      return () => /.+@.+\..+/.test(this.form.email) || '아이디(이메일)는 이메일 형식으로 입력해주세요.'
    },
    passwordConfirmationRule() {
      return () => (this.form.pw === this.rePassword) || '비밀번호가 일치하지 않습니다.'
    },
    enable() {
      if (this.emailRules() == true && this.passwordConfirmationRule() == true && this.min_pw() == true && !!this.form.gender == true && !!this.form.date == true) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style scoped>
  >>> .v-text-field__slot {
    margin: 10px;
  }

  >>> .v-messages__message {
    margin-top: 2px;
  }
  
  >>> .mdi-calendar {
    margin-top: 20px;
  }
</style>