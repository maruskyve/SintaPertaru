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

// Show failed alert if request status is 0
if (rst === '0') {
    CustomAlert.showBottomRightFailedAlert(rmg)
} else if (rst === '1') {  // Show success alert if request status is 1
    CustomAlert.showBottomRightSuccessAlert(rmg)
}