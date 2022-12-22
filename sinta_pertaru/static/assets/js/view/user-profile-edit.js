$(document).ready(() => {
    // User Profile Update Confirmation Modal
    CustomModal.showYesNoFormSubmitModal('userUpdateProfileButton',
        'userUpdateProfileForm',
        'Konfirmasi Perbarui Profil',
        'Rubah Profil sekarang juga?'
    )

    // User Change Password Confirmation Modal
    CustomModal.showYesNoFormSubmitModal('userChangePasswordButton',
        'userUpdatePasswordForm',
        'Konfirmasi Rubah Kata Sandi',
        'Rubah Kata Sandi sekarang juga?')
})