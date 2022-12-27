const test_table_id = 'testDataTable'
const test_add_table_row_id = 'testTableAddRow'
const test_truncate_table_id = 'testTableTruncate'
const test_clear_suitability = 'testTableClearSuitability'
const train_table_id = 'trainDataTable'
const train_add_table_row_id = 'trainTableAddRow'
const train_truncate_table_id = 'trainTableTruncate'
const train_clear_suitability = 'trainTableClearSuitability'


// Action - TEST add table data row
$(`#${test_add_table_row_id}`).on('click', () => {
    let table_row_count = getTableRowCount(test_table_id) + 1;
    let row_template = `<tr id="testDataTableRow${table_row_count + 1}">
                            <!-- Set Test Row Id here!!! -->
                            <td>
                                <div class="form-group">
                                    <label for="testId"></label>
                                    <input class="form-control border-color-left-gray"
                                           id="testId" name="land_data_id" type="hidden">
                                    <label for="testAccuracy"></label>
                                    <input class="form-control border-color-left-gray"
                                           id="testAccuracy" name="land_data_accuracy" 
                                           type="hidden" value="0">
                                    <label for="testObjectId"></label>
                                    <input class="form-control border-color-left-gray required"
                                           id="testObjectId" name="land_data_object_id"
                                           type="text" placeholder="Masukkan Object ID" required>
                                </div>
                            </td>
                            <td>
                                <div class="form-group">
                                    <label for="testRainfall"></label>
                                    <select class="form-control" id="testRainfall"
                                            name="land_data_rainfall">
                                        <option value="< 1.000">< 1.000</option>
                                        <option value="1.000 - 2.000">1.000 - 2.000</option>
                                        <option value="2.000 - 2.500">2.000 - 2.500</option>
                                        <option value="2.500 - 3.000">2.500 - 3.000</option>
                                        <option value="3.000 - 3.500">3.000 - 3.500</option>
                                        <option value="> 3.500">> 3.500</option>
                                    </select>
                                </div>
                            </td>
                            <td>
                                <div class="form-group">
                                    <label for="testSlopes"></label>
                                    <select class="form-control" id="testSlopes" name="land_data_slopes">
                                        <option value="(0 - 3)%">(0 - 3)%</option>
                                        <option value="(3 - 8)%">(3 - 8)%</option>
                                        <option value="(8 - 15)%">(8 - 15)%</option>
                                        <option value="(15 - 25)%">(15 - 25)%</option>
                                        <option value="(25 - 45)%">(25 - 45)%</option>
                                        <option value="> 45%">> 45%</option>
                                    </select>
                                </div>
                            </td>
                            <td>
                                <div class="form-group">
                                    <label for="testSoilType"></label>
                                    <select class="form-control" id="testSoilType"
                                            name="land_data_soil_type">
                                        <option value="Andic Eutropepts">Andic Eutropepts</option>
                                        <option value="Pemukiman">Pemukiman</option>
                                        <option value="Typic Eutropepts">Typic Eutropepts</option>
                                        <option value="Typic Tropaquepts">Typic Tropaquepts</option>
                                        <option value="Typic Troporthents">Typic Troporthents
                                        </option>
                                        <option value="Typic Ustorthents">Typic Ustorthents</option>
                                        <option value="Andic Dystropepts">Andic Dystropepts</option>
                                        <option value="Andic Hapludolls">Andic Hapludolls</option>
                                        <option value="Typic Fragiaquents">Typic Fragiaquents
                                        </option>
                                        <option value="Typic Hapluderts">Typic Hapluderts</option>
                                        <option value="Typic Hapludands">Typic Hapludands</option>
                                        <option value="Typic Fluvaquents">Typic Fluvaquents</option>
                                        <option value="Typic Tropofluvents">Typic Tropofluvents
                                        </option>
                                        <option value="Lithic Ustorthents">Lithic Ustorthents
                                        </option>
                                        <option value="Typic Endoaquents">Typic Endoaquents</option>
                                        <option value="Lithic Ustropepts">Lithic Ustropepts</option>
                                        <option value="singkapan batuan">singkapan batuan</option>
                                        <option value="Typic Ustropepts">Typic Ustropepts</option>
                                        <option value="Kawasan militer">Kawasan militer</option>
                                        <option value="Vertic Tropaquepts">Vertic Tropaquepts
                                        </option>
                                        <option value="Typic Haplusterts">Typic Haplusterts</option>
                                        <option value="Lahan kritis">Lahan kritis</option>
                                        <option value="Fluvaquentic Eutropepts">
                                            Fluvaquentic Eutropepts
                                        </option>
                                        <option value="Aeric Tropaquepts">Aeric Tropaquepts</option>
                                        <option value="Vertic Eutropepts">Vertic Eutropepts</option>
                                    </select>
                                </div>
                            </td>
                            <td>
                                <div class="form-group">
                                    <label for="testSuitability"></label>
                                    <select class="form-control"
                                            id="testSuitability"
                                            name="land_data_suitability" style="width: fit-content; max-width: 250px; ">
                                        <option value="Kawasan Tanaman Semusim dan Permukiman">
                                            Kawasan Tanaman Semusim dan
                                            Permukiman
                                        </option>
                                        <option value="Kawasan Hutan Produksi Tetap/Kawasan Hutan Produksi Konversi/Budidaya Tanaman Tahunan">
                                            Kawasan Hutan Produksi
                                            Tetap/Kawasan Hutan Produksi
                                            Konversi/Budidaya Tanaman
                                            Tahunan
                                        </option>
                                        <option value="Kawasan Fungsi Penyangga/Hutan Produksi Terbatas">
                                            Kawasan Fungsi
                                            Penyangga/Hutan
                                            Produksi Terbatas
                                        </option>
                                        <option value="Kawasan Lindung, termasuk hutan lindung">
                                            Kawasan Lindung, termasuk
                                            hutan
                                            lindung
                                        </option>
                                        <option value="" selected>
                                        </option>
                                    </select>
                                </div>
                            </td>
                            <td>
                                <!-- Test Data Table Row Action -->
                                <div class="form-group text-center">
                                    <!-- Action - Delete Table Row -->
                                    <button class="btn btn-outline-danger rounded-pill btn-sm"
                                            type="button"
                                            onclick="removeElement('testDataTableRow${table_row_count + 1}');">
                                        <i class="">
                                            <svg width="20"
                                                 xmlns="http://www.w3.org/2000/svg"
                                                 class="h-6 w-6" fill="none"
                                                 viewBox="0 0 24 24"
                                                 stroke="currentColor" stroke-width="2">
                                                <path stroke-linecap="round"
                                                      stroke-linejoin="round"
                                                      d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                            </svg>
                                        </i>
                                    </button>
                                </div>
                            </td>
                        </tr>`;
    $(`#${test_table_id} tbody`).prepend(row_template);
    onTableEmpty(test_table_id, 'testTableEmptyRowAlert')
})

// Action - TRAIN add table data row
$(`#${train_add_table_row_id}`).on('click', () => {
    let table_row_count = getTableRowCount(train_table_id) + 1;
    let row_template = `<tr id="trainDataTableRow${table_row_count + 1}">
                            <td>
                                <div class="form-group">
                                    <label for="trainId"></label>
                                    <input class="form-control border-color-left-gray"
                                           id="trainId" name="land_data_id" type="hidden">
                                    <label for="trainAccuracy"></label>
                                    <input class="form-control border-color-left-gray"
                                           id="trainAccuracy" name="land_data_accuracy"
                                           type="hidden" value="0">
                                    <label for="trainObjectId"></label>
                                    <input class="form-control border-color-left-gray"
                                           id="trainObjectId"
                                           name="land_data_object_id"
                                           type="text"
                                           placeholder="Masukkan Object Id" required>
                                </div>
                            </td>
                            <td>
                                <div class="form-group">
                                    <label for="trainRainfall"></label>
                                    <select class="form-control"
                                            id="trainRainfall"
                                            name="land_data_rainfall">
                                        <option value="< 1.000">< 1.000</option>
                                        <option value="1.000 - 2.000">1.000 - 2.000</option>
                                        <option value="2.000 - 2.500">2.000 - 2.500</option>
                                        <option value="2.500 - 3.000">2.500 - 3.000</option>
                                        <option value="3.000 - 3.500">3.000 - 3.500</option>
                                        <option value="> 3.500">> 3.500</option>
                                    </select>
                                </div>
                            </td>
                            <td>
                                <div class="form-group">
                                    <label for="trainSlopes"></label>
                                    <select class="form-control"
                                            id="trainSlopes"
                                            name="land_data_slopes">
                                        <option value="(0 - 3)%">(0 - 3)%</option>
                                        <option value="(3 - 8)%">(3 - 8)%</option>
                                        <option value="(8 - 15)%">(8 - 15)%</option>
                                        <option value="(15 - 25)%">(15 - 25)%</option>
                                        <option value="(25 - 45)%">(25 - 45)%</option>
                                        <option value="> 45 %">> 45 %</option>
                                    </select>
                                </div>
                            </td>
                            <td>
                                <div class="form-group">
                                    <label for="trainSoilType"></label>
                                    <select class="form-control"
                                            id="trainSoilType"
                                            name="land_data_soil_type">
                                        <option value="Andic Eutropepts">Andic Eutropepts</option>
                                        <option value="Pemukiman">Pemukiman</option>
                                        <option value="Typic Eutropepts">Typic Eutropepts</option>
                                        <option value="Typic Tropaquepts">Typic Tropaquepts</option>
                                        <option value="Typic Troporthents">Typic Troporthents
                                        </option>
                                        <option value="Typic Ustorthents">Typic Ustorthents</option>
                                        <option value="Andic Dystropepts">Andic Dystropepts</option>
                                        <option value="Andic Hapludolls">Andic Hapludolls</option>
                                        <option value="Typic Fragiaquents">Typic Fragiaquents
                                        </option>
                                        <option value="Typic Hapluderts">Typic Hapluderts</option>
                                        <option value="Typic Hapludands">Typic Hapludands</option>
                                        <option value="Typic Fluvaquents">Typic Fluvaquents</option>
                                        <option value="Typic Tropofluvents">Typic Tropofluvents
                                        </option>
                                        <option value="Lithic Ustorthents">Lithic Ustorthents
                                        </option>
                                        <option value="Typic Endoaquents">Typic Endoaquents</option>
                                        <option value="Lithic Ustropepts">Lithic Ustropepts</option>
                                        <option value="singkapan batuan">singkapan batuan</option>
                                        <option value="Typic Ustropepts">Typic Ustropepts</option>
                                        <option value="Kawasan militer">Kawasan militer</option>
                                        <option value="Vertic Tropaquepts">Vertic Tropaquepts
                                        </option>
                                        <option value="Typic Haplusterts">Typic Haplusterts</option>
                                        <option value="Lahan kritis">Lahan kritis</option>
                                        <option value="Fluvaquentic Eutropepts">
                                            Fluvaquentic Eutropepts
                                        </option>
                                        <option value="Aeric Tropaquepts">Aeric Tropaquepts</option>
                                        <option value="Vertic Eutropepts">Vertic Eutropepts</option>
                                    </select>
                                </div>
                            </td>
                            <td>
                                <div class="form-group">
                                    <label for="trainSuitability"></label>
                                    <select class="form-control"
                                            id="trainSuitability"
                                            name="land_data_suitability" style="width: fit-content; max-width: 250px; ">
                                        <option value="Kawasan Tanaman Semusim dan Permukiman">
                                            Kawasan Tanaman Semusim dan
                                            Permukiman
                                        </option>
                                        <option value="Kawasan Hutan Produksi Tetap/Kawasan Hutan Produksi Konversi/Budidaya Tanaman Tahunan">
                                            Kawasan Hutan Produksi
                                            Tetap/Kawasan Hutan Produksi
                                            Konversi/Budidaya Tanaman
                                            Tahunan
                                        </option>
                                        <option value="Kawasan Fungsi Penyangga/Hutan Produksi Terbatas">
                                            Kawasan Fungsi
                                            Penyangga/Hutan
                                            Produksi Terbatas
                                        </option>
                                        <option value="Kawasan Lindung, termasuk hutan lindung">
                                            Kawasan Lindung, termasuk
                                            hutan
                                            lindung
                                        </option>
                                    </select>
                                </div>
                            </td>
                            <td>
                                <!-- Train Data Table Row Action -->
                                <div class="form-group text-center">
                                    <!-- Action - Delete Table Row -->
                                    <button class="btn btn-outline-danger rounded-pill btn-sm"
                                            type="button"
                                            onclick="removeElement('trainDataTableRow${table_row_count + 1}');">
                                        <i class="">
                                            <svg width="20"
                                                 xmlns="http://www.w3.org/2000/svg"
                                                 class="h-6 w-6"
                                                 fill="none"
                                                 viewBox="0 0 24 24"
                                                 stroke="currentColor"
                                                 stroke-width="2">
                                                <path stroke-linecap="round"
                                                      stroke-linejoin="round"
                                                      d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                            </svg>
                                        </i>
                                    </button>
                                </div>
                            </td>
                        </tr>`;
    $(`#${train_table_id} tbody`).prepend(row_template);
    onTableEmpty(train_table_id, 'trainTableEmptyRowAlert')
})


// Action - TRAIN truncate table data
$(`#${train_truncate_table_id}`).on('click', () => {
    $(`#${train_table_id} tbody tr`).remove();
    onTableEmpty(train_table_id, 'trainTableEmptyRowAlert')
})

// Action - TRAIn truncate data suitability
$(`#${train_clear_suitability}`).on('click', () => {
    $(`#${train_table_id} tbody tr`).each(function () {
        $(this).find("td:eq(4) option:selected").html("")
    })
})

// Action - TEST truncate table data
$(`#${test_truncate_table_id}`).on('click', () => {
    $(`#${test_table_id} tbody tr`).remove();
    onTableEmpty(test_table_id, 'testTableEmptyRowAlert')
})

// Action - TEST truncate data suitability
$(`#${test_clear_suitability}`).on('click', () => {
    $(`#${test_table_id} tbody tr`).each(function () {
        $(this).find('td:eq(4) option:selected').val('').html("")
    })
})


// Action - TEST process predict
$('#testProcessBtn').on('click', () => {
    $('#testTableProcess').val('1')
    $('#testDataTableForm').submit()
})

// Action - TEST process result
// $('#testProcessResultBtn').on('click', () => {
//
// })

// Action - TEST save changes (temp: wait for pagination solution resolved)
$('#testTableSaveChanges').on('click', () => {
    // $('testDataTableForm').submit((e) => {
    // })
})

$(document).ready(function () {
    // Test data table config
    $('#testDataTable').DataTable({
        // Temporary disable pagination until found to solution to save paginate form
        bPaginate: false,
    });

    // Train data table config
    $('#trainDataTable').DataTable({
        // Temporary disable pagination until solution to save paginate form found
        bPaginate: false
    })

    $('#testProcessBtn').on('click', () => {
        $('#testProcessBtn #processButtonIcon').remove()
        $('#testProcessBtn #processSpinnerIcon').show()
        $('#testProcessBtn span').text('Memproses...')
    })

    // Import csv form submit valid checking


    $('#testDataImportSubmitButton').on('click', () => {
        // If input has a file
        if ($('#testDataImportForm input:file').val()) {
            CustomModal.showProcessingModalDirectly('testDataImportSubmitButton',
                'Mengimpor Data...')
            $('#testDataImportForm').submit()
        }
    })
    $('#vmTrainImportDataSubmitButton').on('click', () => {
        // If input has a file
        if ($('#vmTrainDataImportForm input:file').val()) {
            CustomModal.showProcessingModalDirectly('trainDataImportSubmitButton',
                'Mengimpor Data...')
            $('#vmTrainDataImportForm').submit()
        }
    })

    // Test show / hide process result button
    const pcs_res_btn = $('#testProcessResultBtn')
    // rst === '1' && rst_process === '1' ? pcs_res_btn.show() : pcs_res_btn.hide()

    // Response pop-up
    if (rst === '0') {
        Swal.fire({
            icon: 'error',
            title: 'Terjadi Kesalahan',
            text: rmg,
        })
        pcs_res_btn.show()
    } else if (rst === '1') {
        Swal.fire({
            icon: 'success',
            title: 'Sukses',
            text: rmg,
        })
        pcs_res_btn.show()
    }
});


//
//  Common Function
//

function onTableEmpty(unique_table, unique_alert) {
    let table_row_len = $(`#${unique_table} tbody tr`).length;
    let alert_obj = $(`#${unique_alert}`);

    table_row_len === 0 ? alert_obj.show() : alert_obj.hide()
}

function getTableRowCount(unique_table) {
    return $(`#${unique_table} tbody tr`).length
}

function removeElement(unique_element) {
    $(`#${unique_element}`).remove();
}
