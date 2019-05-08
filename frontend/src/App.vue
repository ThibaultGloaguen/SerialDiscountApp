<template>
    <main id="app">
        <div class="container">

            <div class="content">
                <div class="title">GET YOUR ZATTOO DISCOUNT</div>
                <input type="text" placeholder="Enter your 16 digit code here" ref="inputSerial" v-model="serialNumber">
                <transition name="bounce">
                    <div v-show="errorMessage" class="errorMessage">
                        {{errorMessage}}
                    </div>
                </transition>
                <button class="submit-button" @click="getDiscount">SUBMIT</button>
            </div>

        </div>
        <div class="discount-background" v-if="showDiscountModal" @click="closeDiscountModal">
            <div class="discount-container" @click.stop="">
                <template>
                    <h3>YOUR DISCOUNT CODE</h3>
                    <hr>
                    <div class="discount-box">
                        {{discount}}
                    </div>
                </template>
            </div>

        </div>
    </main>
</template>

<script>
    import httpService from './service/httpService'

    export default {
        name: 'app',
        methods: {
            closeDiscountModal: function () {
                this.showDiscountModal = false
            },
            getDiscount: function () {
                if (!this.serialNumber) {
                    this.$refs["inputSerial"].classList.add('errorClass')
                    this.errorMessage = "Please enter a serial number"
                    return
                }
                httpService.get(`/discount?serial_number=${this.serialNumber}`)
                    .then((res) => {
                        this.errorMessage = ""
                        this.$refs["inputSerial"].classList.remove('errorClass')
                        this.discount = res.data.discount
                        this.showDiscountModal = true
                    })
                    .catch((err) => {
                        this.errorMessage = err.response.data.error
                    })
            }
        },
        data: function () {
            return {
                serialNumber: '',
                discount: 'truc discount',
                errorMessage: '',
                showDiscountModal: false
            }
        }
    }
</script>

<style lang="scss">
    @import "./app.scss";

    .bounce-enter-active {
        animation: bounce-in .3s;
    }

    .bounce-leave-active {
        animation: bounce-out .3s;

    }

    @keyframes bounce-in {
        0% {
            transform: translateX(0);
            opacity: 0;
        }
        25% {
            transform: translateX(15px);
            opacity: 1;
        }
        50% {
            transform: translateX(-10px);
        }
        75% {
            transform: translateX(5px);
        }
        100% {
            transform: translateX(0px);
        }
    }

    @keyframes bounce-out {
        0% {
            transform: translateX(0);
            opacity: 1;
        }
        100% {
            transform: translateX(-25px);
            opacity: 0;
        }
    }
</style>
