const btnOpen = document.querySelector('.open')
const modal  = document.querySelector('.modal')
const btnClose = document.querySelector('.close')


btnOpen.addEventListener('click', OpenModal)
btnClose.addEventListener('click' , closeModal)


function OpenModal (){
    modal.classList.add('show')
}


function closeModal(){
    modal.classList.remove('show')
}