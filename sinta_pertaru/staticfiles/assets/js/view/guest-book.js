// Guest Add Confirmation Modal
CustomModal.showYesNoFormSubmitModal('guestAddButton',
    'guestAddForm',
    'Konfirmasi Tambah Tamu',
    'Tambah Tamu Sekarang?')

// Show failed alert if request status is 0
if (rst === '0') {
    CustomAlert.showBottomRightFailedAlert(rmg)
} else if (rst === '1') {  // Show success alert if request status is 1
    CustomAlert.showBottomRightSuccessAlert(rmg)
}