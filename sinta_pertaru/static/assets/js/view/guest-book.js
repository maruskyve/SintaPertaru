$(document).ready(() => {
    // Guest Add Confirmation Modal
    CustomModal.showYesNoFormSubmitModal('guestAddButton',
        'guestAddForm',
        'Konfirmasi Tambah Tamu',
        'Tambah Tamu Sekarang?')

    // Pop-ups
    if (rst === '0') {
        Swal.fire({
            icon: 'error',
            title: 'Terjadi Kesalahan',
            text: rmg,
        })
    } else if (rst === '1') {
        Swal.fire({
            icon: 'success',
            title: 'Sukses',
            text: rmg,
        })
    }
})