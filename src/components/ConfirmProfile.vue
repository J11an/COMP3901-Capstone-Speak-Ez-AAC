<template>

<div class="v267_1816">
    <div class="v267_1817"></div>
    <div class="BWHelpIcon"> </div>
    <span class="v267_1820">Finish Profile</span>
    <span class="v267_1838">Are you finished setting up your profile?</span>
    <div class="v267_1840">

    </div>
    <span class="v267_1842"@click=handleClick(back)>Back</span>
    <div class="v267_1841">

    </div>
    <span class="v267_1843" @click=handleClick(finish)>Finish</span>
    <div class="v261_18788">
        <div class="v261_18789"></div>
        <div class="v261_18790"></div>
        <div class="v261_18791"><div>
        <div class="v261_18792"></div>
        <div class="v261_18793"></div>
        <div class="v261_18794"></div>
    </div>
    <span class="v284_7712">Tap Finish if done, or click Back to go back to the Categories screen.</span>
    <div class="v472_3774">
        <!-- <div class="v472_3775">
            <div class="v472_3776"></div>
            <span class="v472_3777">Speaking</span>
            <div class="v472_3778">
                <div class="SpeakingScreen"></div>
            </div>
        </div>
        <div class="v472_3780">
            <div class="v472_3781"></div>
            <div class="TypingScreen"></div>
            <span class="v472_3783">Typing</span>
        </div>
        <div class="v472_3784">
            <div class="v472_3785"></div>
            <div class="ListeningScreen"></div>
            <span class="v472_3787">Listening</span>
        </div>
        <div class="v472_3788">
            <div class="v472_3789"></div>
            <span class="v472_3790">Saved Phrases </span>
            <div class="SavedPhrasesScreen"></div>
        </div>
        <div class="v472_3792">
            <div class="v472_3793"></div>
            <span class="v472_3794">Categories</span>
            <div class="Categories"></div>
        </div>
        <div class="v472_3796">
            <div class="v472_3797"></div>
            <div class="LearningScreen"></div>
            <span class="v472_3799">Learning</span>
        </div>
        <div class="v472_3800">
            <div class="v472_3801"></div>
            <div class="ProfileIcon"></div>
            <span class="v472_3803">Profile </span>
        </div>
        <div class="v472_3804">
            <div class="v472_3805"></div>
            <div class="SettingIcon"></div>
            <span class="v472_3807">Settings </span>
        </div>
        <div class="v472_3808">
            <div class="v472_3809"></div>
            <div class="HelpIcon"></div>
            <span class="v472_3811">Help</span>
        </div>
        <div class="name"></div>
        <div class="v472_3813">
            <div class="v472_3814"></div>
            <span class="v472_3815">New/Edit Phrases</span>
            <div class="NewEditScreen"></div>
        </div> -->
        <div class="name"></div>
    </div>
    <div class="name"></div>
</div>

</template>

<script>

export default({
  data() {
    return{
     

    }
  },
  created(){
    this.getCsrToken(); 
    this.Confirm();

  },
  methods:{
    handleClick(keypad){

    },
    Confirm(){
      let self= this
      fetch("api/profile/adduser5",{
        method:'POST',
        body:form_data ,
        errors:[],
        message: '',
        headers:{
          'X-CSRFToken': this.csrf_token
        }
      })
    }

  }
})

</script>

<style>

* {
  box-sizing: border-box;
}
body {
  font-size: 14px;
}
.v267_1816 {
  width: 100%;
  height: 960px;
  background: rgba(255,255,255,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 0px;
  overflow: hidden;
}
.v267_1817 {
  width: 100%;
  height: 91px;
  background: rgba(255,255,255,0.9100000262260437);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 14px;
  box-shadow: 0px 8px 24px rgba(0.5843137502670288, 0.615686297416687, 0.6470588445663452, 0.20000000298023224);
}
.BWHelpIcon {
  width: 143px;
  height: 151px;
  background: url("/public/BWHelpIcon.png");
  opacity: 1;
  position: absolute;
  top: 141px;
  left: 1796px;
}
.v267_1820 {
  width: 216px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 25px;
  left: 17px;
  font-family: Georgia;
  font-weight: Regular;
  font-size: 36px;
  opacity: 1;
  text-align: center;
}
.v267_1838 {
  width: 880px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 221px;
  left: 280px;
  font-family: DM Sans;
  font-weight: Regular;
  font-size: 48px;
  opacity: 1;
  text-align: center;
}
.v267_1840 {
  width: 284px;
  height: 112px;
  background: rgba(255,0,0,1);
  opacity: 1;
  position: absolute;
  top: 596px;
  left: 301px;
  border-top-left-radius: 25px;
  border-top-right-radius: 25px;
  border-bottom-left-radius: 25px;
  border-bottom-right-radius: 25px;
  overflow: hidden;
}
.v267_1842 {
  width: 107px;
  color: rgba(255,255,255,1);
  position: absolute;
  top: 620px;
  left: 393px;
  font-family: DM Sans;
  font-weight: Regular;
  font-size: 48px;
  opacity: 1;
  text-align: center;
}
.v267_1841 {
  width: 284px;
  height: 112px;
  background: rgba(30,195,27,1);
  opacity: 1;
  position: absolute;
  top: 596px;
  left: 835px;
  border-top-left-radius: 25px;
  border-top-right-radius: 25px;
  border-bottom-left-radius: 25px;
  border-bottom-right-radius: 25px;
  overflow: hidden;
}
.v267_1843 {
  width: 128px;
  color: rgba(255,255,255,1);
  position: absolute;
  top: 621px;
  left: 913px;
  font-family: DM Sans;
  font-weight: Regular;
  font-size: 48px;
  opacity: 1;
  text-align: center;
}
.v261_18788 {
  width: 100%;
  height: 36px;
  background: url("/public/v261_18788.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  margin: 4px;
  opacity: 1;
  position: absolute;
  top: 915px;
  left: 203px;
  overflow: hidden;
}
.v261_18789 {
  width: 200px;
  height: 20px;
  background: rgba(71,177,255,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 0px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  overflow: hidden;
}
.v261_18790 {
  width: 200px;
  height: 20px;
  background: rgba(71,177,255,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 204px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  overflow: hidden;
}
.v261_18791 {
  width: 200px;
  height: 20px;
  background: rgba(71,177,255,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 408px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  overflow: hidden;
}
.v261_18792 {
  width: 200px;
  height: 20px;
  background: rgba(71,177,255,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 612px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  overflow: hidden;
}
.v261_18793 {
  width: 200px;
  height: 20px;
  background: rgba(71,177,255,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 816px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  overflow: hidden;
}
.v261_18794 {
  width: 200px;
  height: 20px;
  background: rgba(198,211,234,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 612px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  overflow: hidden;
}
.v284_7712 {
  width: 825px;
  color: url("/public/v284_7712.png");
  position: absolute;
  top: 325px;
  left: 308px;
  font-family: DM Sans;
  font-weight: Regular;
  font-size: 48px;
  opacity: 1;
  text-align: center;
}
.v472_3774 {
  width: 100%;
  height: 92px;
  background: rgba(255,255,255,1);
  opacity: 1;
  position: absolute;
  top: 1px;
  left: 252px;
  overflow: hidden;
}
.v472_3775 {
  width: 116px;
  height: 68px;
  background: url("/public/v472_3775.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 12px;
  left: 14px;
  overflow: hidden;
}
.v472_3776 {
  width: 75px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 20px;
}
.v472_3777 {
  width: 116px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 50px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
}
.v472_3778 {
  width: 38px;
  height: 48px;
  background: url("/public/v472_3778.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 4px;
  left: 38px;
  overflow: hidden;
}
.SpeakingScreen {
  width: 38px;
  height: 48px;
  background: url("/public/SpeakingScreen.png");
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 0px;
}
.v472_3780 {
  width: 75px;
  height: 67px;
  background: url("/public/v472_3780.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 4px;
  left: 151px;
  overflow: hidden;
}
.v472_3781 {
  width: 75px;
  height: 67px;
  background: linear-gradient(rgba(47,224,248,1), rgba(47,176,248,1));
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 0px;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
  overflow: hidden;
}
.TypingScreen {
  width: 38px;
  height: 40px;
  background: url("/public/TypingScreen.png");
  opacity: 1;
  position: absolute;
  top: 5px;
  left: 18px;
}
.v472_3783 {
  width: 66px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 47px;
  left: 4px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
}
.v472_3784 {
  width: 157px;
  height: 68px;
  background: url("/public/v472_3784.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 10px;
  left: 223px;
  overflow: hidden;
}
.v472_3785 {
  width: 75px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 39px;
}
.ListeningScreen {
  width: 40px;
  height: 43px;
  background: url("/public/ListeningScreen.png");
  opacity: 1;
  position: absolute;
  top: 5px;
  left: 58px;
}
.v472_3787 {
  width: 157px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 48px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
}
.v472_3788 {
  width: 155px;
  height: 68px;
  background: url("/public/v472_3788.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 11px;
  left: 459px;
  overflow: hidden;
}
.v472_3789 {
  width: 75px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 39px;
}
.v472_3790 {
  width: 155px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 47px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 11px;
  opacity: 1;
  text-align: center;
}
.SavedPhrasesScreen {
  width: 37px;
  height: 44px;
  background: url("/public/SavedPhrasesScreen.png");
  opacity: 1;
  position: absolute;
  top: 4px;
  left: 59px;
}
.v472_3792 {
  width: 288px;
  height: 68px;
  background: url("/public/v472_3792.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 11px;
  left: 492px;
  overflow: hidden;
}
.v472_3793 {
  width: 75px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 106px;
}
.v472_3794 {
  width: 288px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 45px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
}
.Categories {
  width: 40px;
  height: 45px;
  background: url("/public/Categories.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 4px;
  left: 124px;
  overflow: hidden;
}
.v472_3796 {
  width: 158px;
  height: 69px;
  background: url("/public/v472_3796.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 10px;
  left: 665px;
  overflow: hidden;
}
.v472_3797 {
  width: 75px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 39px;
}
.LearningScreen {
  width: 37px;
  height: 45px;
  background: url("/public/LearningScreen.png");
  opacity: 1;
  position: absolute;
  top: 2px;
  left: 57px;
}
.v472_3799 {
  width: 158px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 42px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
}
.v472_3800 {
  width: 158px;
  height: 72px;
  background: url("/public/v472_3800.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 10px;
  left: 783px;
  overflow: hidden;
}
.v472_3801 {
  width: 75px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 41px;
}
.ProfileIcon {
  width: 31px;
  height: 40px;
  background: url("/public/ProfileIcon.png");
  opacity: 1;
  position: absolute;
  top: 3px;
  left: 63px;
}
.v472_3803 {
  width: 158px;
  color: url("/public/v472_3803.png");
  position: absolute;
  top: 45px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
}
.v472_3804 {
  width: 158px;
  height: 70px;
  background: url("/public/v472_3804.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 11px;
  left: 941px;
  overflow: hidden;
}
.v472_3805 {
  width: 75px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 44px;
}
.SettingIcon {
  width: 38px;
  height: 40px;
  background: url("/public/SettingIcon.png");
  opacity: 1;
  position: absolute;
  top: 5px;
  left: 59px;
}
.v472_3807 {
  width: 158px;
  color: url("/public/v472_3807.png");
  position: absolute;
  top: 45px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
}
.v472_3808 {
  width: 158px;
  height: 71px;
  background: url("/public/v472_3808.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 11px;
  left: 1046px;
  overflow: hidden;
}
.v472_3809 {
  width: 75px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 41px;
}
.HelpIcon {
  width: 34px;
  height: 36px;
  background: url("/public/HelpIcon.png");
  opacity: 1;
  position: absolute;
  top: 8px;
  left: 62px;
}
.v472_3811 {
  width: 158px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 44px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
}
.name {
  color: #fff;
}
.v472_3813 {
  width: 155px;
  height: 68px;
  background: url("/public/v472_3813.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 12px;
  left: 343px;
  overflow: hidden;
}
.v472_3814 {
  width: 75px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 39px;
}
.v472_3815 {
  width: 155px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 47px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 10px;
  opacity: 1;
  text-align: center;
}
.NewEditScreen {
  width: 41px;
  height: 49px;
  background: url("/public/NewEditScreen.png");
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 62px;
}

</style>


