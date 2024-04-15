<template>
    <div id="wrapper">
        <div class="home">
            <div id="test" class="back-row-toggle" style="position: relative;">
                <div class="rain back-row"></div>
            </div>

            <div id="header" class="row">

                <div class="twelve columns">
                    <img class="city" src="../../src/assets/city2_bg.png" alt="" />
                    <img class="glow" src="../../src/assets/glow.png" alt="" />
                    <!--<img class="glow2" src="assets/images/glow2.png" alt="" />-->

                    <div class="container">

                        <div class="row">
                            <div id="logo" class="seven columns">
                                <a href="/"><img class="logo" src="../assets/logo2.png" alt="GangTotz" /></a>
                            </div>

                            <div class="five columns">
                                <div class="menu">

                                    <div class="right">
                                        <a id="about" @click="goto('section1')">About</a>
                                        <a id="faq" @click="goto('section3')">FAQS</a>
                                        <a id="roadmap" @click="goto('section4')">Roadmap</a>
                                        <a id="team" @click="goto('section5')">Team</a>
                                        <a href="https://discord.gg/ckqgggef7j" target="_blank"><img src="../assets/discord.png" alt="" /></a>
                                        <a href="https://twitter.com/GangTotzNFT" target="_blank"><img src="../assets/twitter.png" alt="" /></a>
                                    </div>

                                </div>
                            </div>
                        </div>

                        <div class="row" id="welcome">

                            <div class="twelve columns centerIt">
                                <h1>Welcome to GangTotz</h1>
                                <h4>Only the Strong Survive... Can You?</h4>

                                <div class="box bounce-3">
                                    <a @click="goto('section1')"><img id="scroll" src="../assets/scroll2.png" alt="" /></a>
                                    <p>SCROLL</p>
                                    
                                </div>
                            </div>

                        </div>

                    </div>

                </div>
            </div>
        </div>
      
    </div>
    <!-- begin section 1 -->
    <a href="#" name="section1"></a>
    <div id="section1" ref="section1">
        <!-- begin content container -->
        <div class="twelve columns">

            <div class="container">
                <div  class="six columns">
                  <Carousel :autoplay="2000" :wrap-around="true">
                    <Slide v-for="img in images" :key="img">
                      <div class="carousel__item"><img class="image" :src="require('@/assets/' + img + '.png')"></div>
                    </Slide>        
                  </Carousel>
                </div>
                <div class="six columns intro pad20">
                    <h2>Join the Gang!</h2>
                    <p>
                    Gangtotz is an NFT that depicts diversity, and strength in numbers, no matter what group or "gang" you're born into.
                    This is also how we see our Community. Everyone brings such a vital piece to the space,
                    whether it's through ideas, culture, or&nbsp;perspective. <br /><br />

                    With that being said, we'd love for you to join our Community! If you're interested and want to learn more,
                    come join the Gang on&nbsp;Discord!
                    </p>

                    <div class="buttons">
                            <div class="five columns">
                              <a class="cta" href="https://discord.gg/ckqgggef7j" target="_blank">JOIN DISCORD</a>
                            </div>
                            
                    </div>
                      
                 
                </div>
                
            </div>

        </div>
    </div>
    <!-- end section 1 -->

    <!-- begin section 2 -->
    <a href="#" name="section2"></a>
    <div id="section2" ref="section2">

        <div class="twelve columns">
            <div class="container2">
            <h2>The DNA of a Tot</h2>
            <h4>These Totz Never Had It Easy.</h4>

            <div class="row dna">
                <img src="../assets/animation.gif" width="100%" alt="" />
            </div>
            </div>
        </div>

    </div>
    <!-- end section 2 -->

    <!-- begin section 3 -->
    <a href="#" name="section3"></a>
    <div id="section3" ref="section3">

        <div class="twelve columns">
            <div class="container">

            <div class="pad20">
              <h2>Lil Gangstas in the Making</h2>
              <h4>Bosses aren't born, they're created.</h4>
            </div>

            <!-- ROW 1 -->
            <div class="row making">
                <div class="four columns">
                <img src="../assets/step1.png" width="100%" alt="" />
                <h4>Initial Sketch</h4>
                <h5>The Basic Tot is Here!</h5>
                </div>
                <div class="four columns">
                <img src="../assets/step2.png" width="100%" alt="" />
                <h4>Lineart</h4>
                <h5>Gimme the Lines (Ohh! & Weapons!)</h5>
                </div>
                <div class="four columns">
                <img src="../assets/step3.png" width="100%" alt="" />
                <h4>Final GangTot</h4>
                <h5>Bow Down, The Boss has Arrived.</h5>
                </div>
            </div>

            <div class="row faq">         

                <div class="five columns pad20">
                    <h2>Frequently <br class="hide" /> Asked <br class="hide" /> Questions</h2>
                    <img src="../assets/fulltot.png" alt=""/>
                </div>
                    <div class="seven columns">

                        <ul>
                            <li v-for="item in items" :class="{ active: item.isActive }">
                                <div class="question" @click="toggle(item)"> 
                                    <div id="img-min-plu">
                                        <img v-show="item.showPlus" :src="require('../assets/plus.png')" alt="" id="plus">
                                        <img v-show="item.showMinus" :src="require('../assets/minus.png')" alt="" id="plus">
                                    </div>
                                    <div id="text-question">
                                        {{ item.text }}
                                    </div>
                                </div>
                                <Transition name="slide-fade">
                                    <div v-show="item.isActive" class="answer">   
                                            {{ item.desc }}                                    
                                    </div>
                                </Transition>
                                <div id="line-faq"></div>
                            </li>
                        </ul>

                    </div>
                </div>

            </div>
        </div>

    </div>
    <!-- end section 3 -->

    <!-- begin section 4 -->
    <a href="#" name="section4"></a>
    <div id="section4" ref="section4">

        <div class="twelve columns">
            <div class="container">
                <h2>The Roadmap</h2>
                <p class="details">
                    This is only the beginning!
                    Join us on this Journey of not only learning how far Crypto & NFTs can go,
                    but how far We All Can Go, Together! Strength in Numbers - Gang, Gang!
                </p>

                <!-- ROW 1 -->
                <div class="row roadmap">
                    <div class="four columns">
                    <h4>Community</h4>
                    <h5>Always Building the Community - Discord, Twitter, etc.</h5>
                    </div>
                    <div class="four columns">
                    <h4>Ownership / The Mint</h4>
                    <h5>Minting of the NFTs!</h5>
                    </div>
                    <div class="four columns">
                    <h4>GANG Token</h4>
                    <h5>Planning & Creation of a GangTot Token for further incentives and Holder Benefits.</h5>
                    </div>
                </div>

                <!-- ROW 2 -->
                <div class="row roadmap">
                    <div class="four columns">
                    <h4>Metaverse / Game Friendly</h4>
                    <h5>Begin exploring ideas and/or partnerships for an actual Metaverse or GangTotz Game!</h5>
                    </div>
                    <div class="four columns">
                    <h4>Holder Appreciation</h4>
                    <h5>Giveaways, Airdrops, NFTs, Tokens, & more to Tot Holders!</h5>
                    </div>
                    <div class="four columns">
                    <h4>Staking</h4>
                    <h5>The ability to Stake your NFTs to Earn the Official GangTot Tokens!</h5>
                    </div>
                </div>

                <!-- ROW 3 -->
                <div class="row roadmap">
                    <div class="four columns">
                    <h4>Merchandise</h4>
                    <h5>T-shirts, Hoodies, & More so you can properly Rep' your Gang in the Real World!</h5>
                    </div>
                    <div class="four columns">
                    <h4>Partnerships</h4>
                    <h5>We will always be exploring potential Partnerships + Collabs with other NFTs in the space!</h5>
                    </div>
                    <div class="four columns">
                    <h4>& Much  More!</h4>
                    <h5 id="roadmap-links">Come find out more about us by joining our Community on 
                      <a href="https://discord.gg/ckqgggef7j" target="_blank">Discord</a> &
                      <a href="https://twitter.com/GangTotzNFT" target="_blank">Twitter</a> !
                    </h5>
                    </div>
                </div>

            </div>
        </div>

    </div>
    <!-- end section 4 -->

    <!-- begin section 5 -->
    <a href="#" name="section5"></a>
    <div id="section5" ref="section5">

        <div class="twelve columns">
            <div class="container">
            <h2>Meet the Team</h2>
            <h4>
                Our Team is Built based on a True Friendship. <br />
                We also want this to reflect in our Community. Or better yet, our Gang!
            </h4>

            <!-- ROW 1 -->
            <div class="row team">
                <div class="six columns">
                    <div class="teamPic"><img src="../assets/brian.png" width="100%" alt="" />
                        <span>
                            <h3>GenZod (Brian)</h3>
                            <div id="span-text">
                            Hi, my name is Brian, but most people around the community call me ZOD.
                            I've been an active part of the Cardano Community since late 2017.
                            I'm passionate about Cardano, the Community, and NFTs. Thanks for checking out GangTotz.
                            </div>
                        </span>
                    </div>
                    <h4>Brian</h4>
                    <h5>Co-Founder / Front-end Developer</h5>
                </div>
                <div class="six columns">
                    <div class="teamPic"><img src="../assets/zeek.png" width="100%" alt="" />
                        <span>
                        <h3>Zek (Ezequiel)</h3>
                        <div id="span-text">
                          Hi folks, my name is Ezequiel. I'm a Python/Vue developer who fell in love with Cardano in 2020! 
                          Since that time, my heart belongs to this Ecosystem / Community and learning as much as I can about Blockchain Development. 
                          It's just the Beginning - Long Live Cardano!
                        </div>
                        </span>
                    </div>
                    <h4>Zek</h4>
                    <h5>Co-Founder / Backend + Blockchain Developer</h5>
                </div>
            </div>

            </div>
        </div>

    </div>
   
    <WalletModal v-show="showModal" @close-modal="showModal = false" />   
   
    <a id="select-wallet" @click="showModal = true" v-show="purchaseButton">B</a> 
</template>

<script>
import WalletModal from '../components/WalletModal.vue'
import axios from 'axios'
import { defineComponent } from 'vue'
import { Carousel, Pagination, Slide } from 'vue3-carousel';

import 'vue3-carousel/dist/carousel.css';
export default {
    name: 'HomeView',
    data() {
        return {
            showModal: false,
            purchaseButton: true,
            isactive: false,
            images:['test1', 'test6', 'test5', 'test2', 'test4', 'test7', 'test8'],
            items: [
                {
                    isActive: false,
                    text: 'Which Blockchain will GangTotz be Minted on?',
                    desc: 'Cardano, of course!',
                    showPlus: true,
                    showMinus: false,
                },
                {
                    isActive: false,
                    text: 'When is the Official Drop?',
                    desc: 'Sunday December 4th 2022 at 15:00 Hs. (EST)',
                    showPlus: true,
                    showMinus: false,
                },
                {
                    isActive: false,
                    text: 'How much will each GangTot NFT be to mint?',
                    desc: 'Each NFT will be 60 $ADA to Mint (plus normal Cardano transaction fees).',
                    showPlus: true,
                    showMinus: false,
                },
                {
                    isActive: false,
                    text: 'How many GangTotz will there be?',
                    desc: 'There will be a total of 5,555 GangTotz.',
                    showPlus: true,
                    showMinus: false,
                },
                {
                    isActive: false,
                    text: 'Will there be rarity ranks?',
                    desc: 'Every GangTot will have unique Traits, such as the Gang, hairstyles, clothing, and accessories..However, rarity is in the eye of the beholder.. or the owner in this case!',
                    showPlus: true,
                    showMinus: false,
                },
                {
                    isActive: false,
                    text: "What's the GangTotz policy ID?",
                    desc: '1ae260ca224a439dd84ed8e0a19ef695b17637f279fe650465870326',
                    showPlus: true,
                    showMinus: false,
                },
                {
                    isActive: false,
                    text: 'Which wallets can I use?',
                    desc: 'You can use Nami, Eternl, Flint, or Yoroi for Minting.',
                    showPlus: true,
                    showMinus: false,
                },
                {
                    isActive: false,
                    text: 'How do I Mint?',
                    desc: 'On Offical Mint Day, there will be a Select Wallet / Buy Button. Once you press the Button,\
                          You will be asked to Select which Wallet you want to use to Buy. Please note, you must connect a dApp enabled wallet, such as Nami,\
                          eternl, Flint, or Yoroi. After your Wallet selection, the price of the GangTot will be displayed in your wallet for you to Sign / Submit the\
                          Transaction. You should receive your NFT anywhere between 1 minute & 3 Hours after you Mint (Depending on Blockchain speed and conditions).',
                    showPlus: true,
                    showMinus: false,
                },
                {
                    isActive: false,
                    text: 'Do you have social media accounts?',
                    desc: 'Absolutely! Follow us on Twitter, and check out our Discord!',
                    showPlus: true,
                    showMinus: false,
                }
            ],
        }
    },
    components: { 
        WalletModal,
        Carousel,
        Slide,
        Pagination
    },
    mounted() {
        this.makeItRain(),
        this.teamPic(),
        this.checkTkAmount()
    },
    methods: {
        teamPic() {
          $(".teamPic").hover(function() {
            $(this).find('span').animate({'bottom': '0%'},500);
          }, function() {
            $(this).find('span').animate({'bottom': '-100%'},300);
          });
        },
        makeItRain() {
        //clear out everything
        $('.rain').empty();
        var increment = 0;
        var drops = "";
        var backDrops = "";
        while (increment < 1000) {
            //couple random numbers to use for various randomizations
            //random number between 98 and 1
            var randoHundo = (Math.floor(Math.random() * (98 - 1 + 1) + 1));
            //random number between 5 and 2
            var randoFiver = (Math.floor(Math.random() * (.5 - 2 + 1) + 2));
            //increment
            increment += randoFiver;
            //add in a new raindrop with various randomizations to certain CSS properties
            drops += '<div class="drop" style="left: ' + increment + '%; bottom: ' + (randoFiver + randoFiver - 1 + 100) + '%; animation-delay: 0.' + randoHundo + 's; animation-duration: 0.5' + randoHundo + 's;"><div class="stem" style="animation-delay: 0.' + randoHundo + 's; animation-duration: 0.5' + randoHundo + 's;"></div><div class="splat" style="animation-delay: 0.' + randoHundo + 's; animation-duration: 0.5' + randoHundo + 's;"></div></div>';
            backDrops += '<div class="drop" style="right: ' + increment + '%; bottom: ' + (randoFiver + randoFiver - 1 + 100) + '%; animation-delay: 0.' + randoHundo + 's; animation-duration: 0.5' + randoHundo + 's;"><div class="stem" style="animation-delay: 0.' + randoHundo + 's; animation-duration: 0.5' + randoHundo + 's;"></div><div class="splat" style="animation-delay: 0.' + randoHundo + 's; animation-duration: 0.5' + randoHundo + 's;"></div></div>';
        }
        $('.rain.front-row').append(drops);
        $('.rain.back-row').append(backDrops);
        setTimeout( function(){ $(".rain").css("visibility","visible"); }, 2000);
        },
        getNfts() {
            axios
                .get('nfts')
                .then(response => {
                    this.nfts = response.data
                    console.log('data:', response.data)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        goto(refName) {
            var element = this.$refs[refName];
            var top = element.offsetTop;
            window.scrollTo({
              top: top,
              behavior: 'smooth',
            });
        },
        toggle(item) {
            item.isActive = !item.isActive;
            this.isactive = !this.isactive;
            item.showPlus = !item.showPlus;
            item.showMinus = !item.showMinus;   
        },
        checkTkAmount() {
          axios.get('available_nfts').then(response => {
            console.log(response.data)
            if(response.data > 0){
              this.purchaseButton = true
            }else{
              this.purchaseButton = false
            }
          })
        }
                
    }  
}
</script>


<style>

@import url('https://fonts.googleapis.com/css2?family=Corben:wght@700&family=Roboto:wght@400;500;700;900&display=swap');

.carousel__slide > .carousel__item {
  transform: scale(1);
  opacity: 0.5;
  transition: 0.5s;
}
.carousel__slide--visible > .carousel__item {
  opacity: 1;
  transform: rotateY(0);
}
.carousel__slide--next > .carousel__item {
  transform: scale(0.9) translate(-10px);
}
.carousel__slide--prev > .carousel__item {
  transform: scale(0.9) translate(10px);
}
.carousel__item img{
  width:400px;
}

#select-wallet{
    cursor: pointer;
    color: #000000;
}

html { margin: 0px; padding: 0px; }
body { margin: 0px; background-color: #000000; }

h1 { font-size: 60px; margin: 50px 0px 0px 0px; color: #db3636; }
h2 { font-size: 30px; margin: 0px 0px 3px 0px; color: #FFFFFF; text-transform: uppercase; letter-spacing: .5px }
h3 { font-size: 26px; }
h4 { font-size: 17px; font-weight: normal; color: #909090; margin: 0px 0px 55px 0px; }

h1, h2 {
  font-family: 'Corben', 'Roboto', Arial !important;
}

ul {
    list-style-type: none;
}
ul li { margin: 0px; padding: 0px; }

.logo { width: 250px; }

.centerIt { width: 100%; text-align: center; }
.left { float: left; }
.right { float: right;}
.bold { font-weight: 600; }

p { margin: 0px 0px 30px 0px; color: #909090; }
p a { color: #fff110; }
p a:hover { color: #fff110; text-decoration: underline; }

.menu { padding: 40px 0px 0px 0px; }
.menu a {
  color: #db3636;
  text-transform: uppercase;
  font-size: 15px;
  font-weight: 600;
  text-decoration: none;
  float: left;
  cursor: pointer;
}

.menu a:last-child { margin-right: 0px; }
.menu img, #footer img {
  width: 20px;
  margin-top: 3px;
}
.menu a:hover {color: #db3636;}

#header {
  width: 100%;
  padding: 25px 0px 0px 0px;
  background: rgb(25,34,80);
  background: linear-gradient(360deg, rgba(25,34,80,1) 13%, rgba(0,0,0,1) 94%);
  /*background: url('../images/intro_bg.png') #192250;
  background-size: contain;*/
  min-height: 800px;
  position: relative;
}
.box {
  animation-duration: 1.5s;
  animation-iteration-count: infinite;
  width: 150px;
  height: 35px;
  margin: 0 auto;
  transform-origin: bottom;
  top: 20px;
  position: relative;
  text-align: center;
}
.box img { width: 35px; margin: 0px auto 7px auto; clear: both; display: block; }
.bounce-3 {
 animation-name: bounce-3;
 animation-timing-function: ease-in-out;
 cursor: pointer;
}
.bounce-3 p{
  margin-top: -30px;
  color: #000000;
}
@keyframes bounce-3 {
 0%   { transform: translateY(0); }
 50%  { transform: translateY(-20px); }
 100% { transform: translateY(0); }
}

.glow, .glow2, .city {
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 100%;
}
.glow, .glow2 {
  mix-blend-mode:hard-light;
  opacity: 1;
}

.city { z-index: 990; }
.glow, .glow2 { z-index: 0; }

#section1, #section3, #section5 {
  width: 100%;
  background-color: #000000;
  float: left;
  clear: both;
  overflow: hidden;
}
#section2, #section4 {
  width: 100%;
  background-color: #1b1b1b;
  padding: 35px 0px 0px 0px;
  float: left;
  clear: both;
  overflow: hidden;
}
#section1, #section3, #section4, #section5 { padding: 35px 0px 75px 0px; }
#section2, #section3, #section4, #section5 { text-align: center; }

#section1 p { font-size: 18px; letter-spacing: 0px; line-height: 24px; }
#section2 h4 { margin-bottom: 15px; }

.dna img {
  width: 95%;
  margin: 0px auto;
  position: relative;
  top: 10px;
}

#mainPhoto{
    width: 100%;
}

.container a{
  margin-right: 22px;  
}

/* FAQ STYLES */

.faq img{
    width: 60%;
}
.faq {
  text-align: left !important;
  overflow: hidden;
}
.faq h2 {
  text-align: left;
  font-size: 40px;
  line-height: 54px;
  margin-bottom: 50px;
  padding-top: 25px;
}
.faq .question {
  display: block;
  padding: 23px 0px 23px;
  color: #FFFFFF;
  font-weight: bold;
  font-size: 18px;
  cursor: pointer;
}
.faq .answer {
  margin-left: 23px;
  margin-bottom: 15px;
  margin-top: -20px;
  font-size: 18px;
  color: #909090;
}
#plus{
    width: 14px;
    padding-right: 10px;
}
#line-faq{
  border-bottom: 1px solid #1b1b1b;
}
#img-min-plu, #text-question{
    display: inline;
}

/*
  Enter and leave animations can use different
  durations and timing functions.
*/
.slide-fade-enter-active {
  transition: all 0.4s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.4s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}


/* ROADMAP STYLES */
.roadmap {
  text-align: center!important;
  overflow: hidden;
  margin: 0px 0px 100px 0px;
}
.roadmap h4 {
  font-size: 22px;
  line-height: 26px;
  color: #db3636;
  margin: 0px;
  font-weight: 900;
}
.roadmap h5 {
  font-size: 18px;
  line-height: 22px;
  color: #909090;
  margin: 0px;
  font-weight: normal;
}
#roadmap-links a {
  color: #db3636;
  text-transform: uppercase;
  font-size: 15px;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  margin-right: 0px;
}
p.details {
  font-size: 18px;
  line-height: 26px;
  font-weight: normal;
  color: #FFFFFF;
  margin: 20px auto 55px auto;
  width: 55%;
}

#section4 .twelve{
  margin-bottom: -95px;
}

/* MAKING STYLES */
.making {
  text-align: left;
  overflow: hidden;
  margin: 0px 0px 100px 0px;
}
.making h4 {
  font-size: 18px;
  line-height: 20px;
  color: #FFFFFF;
  margin: 0px;
  font-weight: 700;
}
.making h5 {
  font-size: 16px;
  line-height: 18px;
  color: #909090;
  margin: 0px;
  font-weight: normal;
}

/* TEAM STYLES */
.team {
  text-align: left;
  overflow: hidden;
  margin: 0px 0px 50px 0px;
}
.team h4 {
  font-size: 18px;
  line-height: 20px;
  color: #FFFFFF;
  margin: 0px;
  font-weight: 700;
}
.team h5 {
  font-size: 18px;
  line-height: 20px;
  color: #909090;
  margin: 0px;
  font-weight: normal;
}

.teamPic {
  position: relative;
  cursor: pointer;
  overflow: hidden;
}
.teamPic span {
  position: absolute;
  bottom: -50%;
  left: 0px;
  width: 100%;
  height: 40%;
  background: #000000;
  color: #FFFFFF !important;
  opacity: .85;
  padding: 20px;
}

.teamPic h3 {
  margin: 0px 0px 5px 0px;
  color: #db3636;
}
.teamPic h4 {
  color: #db3636;
  margin: 0px;
}

#span-text{
  width: 90%;
}

/* CTA STYLE */
.cta {
  padding: 18px 23px 18px 18px;
  color: #000000;
  font-size: 16px;
  background-color: #db3636;
  font-weight: 900;
  text-decoration: none;
  clear: both;
  max-width: 175px;
  text-align: center;
  display: block;
  cursor: pointer;
}
.cta:hover { color: #000000; }



/*RAIN*/
.rain {
  position: absolute;
  left: 0;
  top: 320px;
  width: 100%;
  height: 420px;
  z-index: 5;
  overflow: hidden;
}
.rain.back-row {
  display: none;
  z-index: 4;
  bottom: 0px;
  opacity: 0.5;
}
#test.back-row-toggle .rain.back-row {
  display: block;
  visibility: hidden;
}
.drop {
  position: absolute;
  bottom: 100%;
  width: 15px;
  height: 100px;
  pointer-events: none;
  animation: drop 0.5s linear infinite;
}
@keyframes drop {
  0% { transform: translateY(0vh); }
  75% { transform: translateY(70vh); }
  100% { transform: translateY(70vh); }
}
.stem {
  width: 1px;
  height: 60%;
  margin-left: 7px;
  background: linear-gradient(to bottom, rgba(255, 255, 255, 0), rgba(255, 255, 255, .30));
  animation: stem 0.5s linear infinite;
}
@keyframes stem {
  0% { opacity: 1; }
  65% { opacity: 1; }
  75% { opacity: 0; }
  100% { opacity: 0; }
}


@media only screen and (max-width: 1035px),
	(min-device-width: 449px) and (max-device-width: 1035px){

    #select-wallet { display: none; }

    .seven.columns{
      width: 100%;
    }

    #logo{
      text-align: center;
    }

    .logo{
      width: 200px;
    }

    #header{
      min-height: 600px;
    }

    #header h1{
      font-size: 40px;
    }

    #header .twelve{
      margin-top: -10px;
    }

    #header .five.columns{
      display: none;
    }

    .box{
      margin-top: -40px;
      -webkit-tap-highlight-color: transparent;
    }

    .carousel__item img{
      width:300px;
    }

    #section1 .five.columns{
      width: 100%;
    }

    #section1 .twelve{
      margin-top: -20px;
    }

    #section1 p{
      font-size: 15px;
      line-height: 19px;
    }

    .cta{
      margin-top: -18px;
    }

    #section1 h2{
      font-size: 25px;
    }

    #section3 .five.columns{
      width: 40%; 
    }

    .faq .seven.columns{
      float: right;
      width: 50%; 
    }

    .faq{
      margin-top: -30px;
    }

    .faq h2{
      font-size: 30px;
    }

    .faq .question{
      text-align: center;
      -webkit-tap-highlight-color: transparent;
    }

    #text-question{
      font-size: 15px;
    }
    .faq .answer{
      text-align: center;
      font-size: 15px;
    }

    #section3, #section5{
      margin-bottom: -50px;
    }

    #section4{
      margin-bottom: -90px;
    }

    #section4 .twelve{
      margin-bottom: -45px;
    }

    p.details{
      width: 100%;
    }

    .making div, .team div {
      -webkit-tap-highlight-color: transparent;
    }
    .teamPic span {
      height: 160px;
      bottom: -100%;
    }
    #span-text{
      font-size: 12px;
    }

    .rain{
      top: 250px;
      height: 1000px;
    }

}

@media only screen and (max-width: 448px),
    (min-device-width: 200px) and (max-device-width: 448px) {

  .pad20 { padding: 0px 20px; }
  #select-wallet { display: none; }
  #header { min-height: 430px; }
  #logo { text-align: center; }
  .logo {
    margin: 0px auto !important;
    text-align: center !important;
    width: 170px;
  }

  #header h4{
    margin-block-start: 10px;
  }

  .hide { display: none; }

  #section1, #section2, #section3, #section4, #section5 { text-align: center; }

  .intro { margin-top: 30px; }

  h1 { font-size: 32px; }
  h2 { font-size: 24px; line-height: 30px; }
  h4 { margin-bottom: 25px; }

  #section1 p { font-size: 16px; line-height: 24px; }
  p.details {
    margin: 20px auto 55px auto;
    width: 85%;
  }
  .container a {
    margin-right: auto;
    margin-left: auto;
  }

  .box{
    -webkit-tap-highlight-color: transparent;
    margin-top: 0;
  }

  .bounce-3 p{
    margin-top: 0;
  }

  .carousel__item img{
    width:300px;
  }

  .cta{

      padding: 18px 23px 18px 18px;
    }

  #section3 .five.columns{
      width:100%; 
  }
  .faq .seven.columns {
    width: 100%;
  }

  .faq h2 { font-size: 28px; line-height: 34px; padding: 0px; }
  .faq h2, .making, .team { text-align: center; }
  .faq img { width: 50%;  }
  .faq {
    text-align: center !important;
  }

  .question{
    text-align: center;
    -webkit-tap-highlight-color: transparent;
  }

  .faq .answer{
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    width: 80%;
  }

  #plus{
    width: 15px;
  }

  #text-question{
    margin-left: auto;
    margin-right: auto;
  }

  #line-faq{
    margin-left: auto;
    margin-right: auto;
    width: 80%;
  } 

  .making { margin: 0px 0px 40px 0px; }
  .making div, .team div {
    -webkit-tap-highlight-color: transparent;
  }
  .making h5{margin-bottom: 15px;}
  .making h4{margin-top: 5px;}
  .teamPic span {
  bottom: -100%;  
  height: 60%;
  }
  .team h5{margin-bottom: 15px;}
  .roadmap { margin-bottom: 15px; text-align: center !important; }
  .roadmap div { margin: 0px 0px 15px 0px; }
  #section4 .twelve{
    margin-bottom: 20px;
  }
  .team { margin: 0px 0px 20px 0px !important; }

  .cta { margin: 0px auto; }
  .menu { display: none; }

  #footer { text-align: center; }
  .footMenu {
    margin: 10px auto 0px auto;
    text-align: center;
  }

  #select-wallet{
    margin-top: 30px;
  }

  .rain{
    top: 290px;
    height: 150px;
  }
}




</style>