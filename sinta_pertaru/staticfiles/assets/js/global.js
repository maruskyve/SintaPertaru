if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}

// On logout button clicked
$('.logoutBtn').on('click', () => {
    $('.logoutConfirmationModal').modal()
})

// Password toggler (show / hide)
$('.passwordInputToggler').on('click', () => {
    let obj_up = $('.passwordInput')
    if (obj_up.prop('type') === 'password') {
        obj_up.attr('type', 'text')
        $('.passwordInputToggler i svg').remove()
        $('.passwordInputToggler i').append(`<svg width="20" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21" />
                </svg>`)
    } else {
        obj_up.attr('type', 'password')
        $('.passwordInputToggler i svg').remove()
        $('.passwordInputToggler i').append(`<svg width="20" xmlns="http://www.w3.org/2000/svg"
                     class="h-6 w-6"
                     fill="none" viewBox="0 0 24 24" stroke="currentColor"
                     stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round"
                          d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round"
                          d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                </svg>`)
    }
})


class CustomModal {
    static showYesNoFormSubmitModal(unique_caller,
                                    unique_form,
                                    modal_title,
                                    modal_body) {
        let modal_template =
            `<div class="modal fade" id="${unique_caller}Modal" tabindex="-1"
                 role="dialog" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered modal-sm">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">${modal_title}</h5>
                            <button type="button" class="close" data-dismiss="modal"
                                    aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <p>${modal_body}</p>
                        </div>
                        <div class="modal-footer">
                            <button type="button"
                                    class="btn btn-danger rounded-pill"
                                    data-dismiss="modal">
                                Batal
                            </button>
                            <button type="submit" class="btn btn-dark rounded-pill"
                                    form="${unique_form}">Ya
                            </button>
                        </div>
                    </div>
                </div>
            </div>`

        // Executed once
        let uc_obj = '#' + unique_caller

        $(uc_obj).one('click', () => {
            $('body').append(modal_template)
        })

        // Show Modal
        $(uc_obj).on('click', () => {
            $(`#${unique_caller}Modal`).modal('show')
        })
    }

    static #processingModalTemplate(modal_id,
                                    modal_body,
                                    spinner_type) {
        const spinner_map = {
            0: 'fa-spinner',
            1: 'fa-circle-notch',
            2: 'fa-loader'
        }
        return `<div class="modal fade" id="${modal_id}" tabindex="-1"
                     role="dialog" aria-hidden="true" style="">
                    <div class="modal-dialog modal-dialog-centered modal-sm">
                        <div class="modal-content">
                            <div class="modal-body">
                            <i class="fa ${spinner_map[spinner_type]} faa-spin animated"
                               aria-hidden="true"></i>
                               <span>${modal_body}</span>
                            </div>
                        </div>
                    </div>
                </div>`
    }

    static showProcessingModal(unique_caller,
                               modal_body,
                               spinner_type = 0) {
        let modal_id = unique_caller + 'Modal'
        let modal_template = this.#processingModalTemplate(modal_id, modal_body, spinner_type)

        $('body').append(modal_template)

        //when modal opens and close
        $(`#${modal_id}`).on('shown.bs.modal', function (e) {
            $("body").css({opacity: 0.5});
        }).on('hidden.bs.modal', function (e) {
            $("body").css({opacity: 1});
        })

        // Executed once
        let uc_obj = '#' + unique_caller

        // Show Modal
        $(uc_obj).on('click', () => {
            $(`#${modal_id}`).modal('show')
        })
    }

    static showProcessingModalDirectly(unique,
                                       modal_body,
                                       spinner_type = 0) {
        let modal_id = unique + 'Modal'
        let modal_template = this.#processingModalTemplate(modal_id, modal_body, spinner_type)

        $('body').append(modal_template)

        //when modal opens and close
        $(`#${modal_id}`).on('shown.bs.modal', function (e) {
            $("body").css({opacity: 0.5});
        }).on('hidden.bs.modal', function (e) {
            $("body").css({opacity: 1});
        }).modal('show')
    }
}

class CustomAlert {
    static #alertTemplate(alert_position,
                          alert_body,
                          is_success) {
        return `<div class="fixed-bottom">
                    <div class="alert alert-dismissible float-${alert_position} bg-white basic-drop-shadow rounded-pill fade m-2 w-25 p-0 show"
                         role="alert" style="right: 20px;">
                             <img src="${is_success ? success_1_icon : failed_1_icon}" class="img-fluid rounded-pill" width="60" height="20"
                             alt="asd">
                        <span class="mt-sm-3">${alert_body}</span>
                        <button type="button" class="close rounded-pill text-secondary p-1" data-dismiss="alert"
                                aria-label="Close">
                            <i class="fa faa-shake faa-slow animated">
                                <span aria-hidden="true">
                                    <svg width="20" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                                         stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"></path>
                                    </svg>
                                </span>
                            </i>
                        </button>
                    </div>
                </div>`
    }

    static showBottomLeftSuccessAlert(alert_body) {
        $('body').append(this.#alertTemplate('left', alert_body, true))
    }

    static showBottomRightSuccessAlert(alert_body) {
        $('body').append(this.#alertTemplate('right', alert_body, true))
    }

    static showBottomLeftFailedAlert(alert_body) {
        $('body').append(this.#alertTemplate('left', alert_body, false))
    }

    static showBottomRightFailedAlert(alert_body) {
        $('body').append(this.#alertTemplate('right', alert_body, false))
    }
}
