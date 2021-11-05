const faqsBox = document.getElementById('faqs-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('loadmoreBtn')
const loadBox = document.getElementById('loading-box')
let visible = 3

const handleGetData = () => {
    $.ajax({
        type: 'GET',
        url: `/faqs-json/${visible}/`,
        success: function (response) {
            // console.log(response.max)
            max_size = response.max
            const data = response.data
            spinnerBox.classList.remove('not-visible')
            setTimeout(() => {
                spinnerBox.classList.add('not-visible')
                data.map(faq => {
                    console.log(faq.id)
                    faqsBox.innerHTML += 
                
                    `<div class="faq">
                        <div class="question">
                            <h3>${ faq.question }</h3>

                            <svg width="15" height="10" viewBox="0 0 42 25">
                                <path d="M3 3L21 21L39 3" stroke="white" stroke-width="7" stroke-linecap="round" />
                            </svg>
                        </div>
                        <div class="answer">
                            <p>${ faq.answer }</p>
                        </div>
                    </div>`
                })
            }, 500)
            if(max_size) {
                console.log('done')
                // loadBox.innerHTML = 
            }
        },
        error: function (error) {
            console.log(error)
        }
    })
}

handleGetData()

loadBtn.addEventListener('click', () => {
    visible += 3
    handleGetData()
})