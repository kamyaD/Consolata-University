# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class FileUpload(models.Model):
    file_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'file_upload'


class IctInventory(models.Model):
    item = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    received = models.CharField(max_length=100)
    issued = models.CharField(max_length=100)
    balance = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    incharge = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ict_inventory'


class TblAbc(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    days = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_abc'


class TblAppointments(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    entry_date = models.CharField(max_length=50)
    venue = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_appointments'


class TblApprovedClearance(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=250)
    user_name = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField()
    approval_status = models.CharField(max_length=20)
    date_paid = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_approved_clearance'


class TblApprovedInvoices(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=250)
    user_name = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField()
    payment_status = models.CharField(max_length=10)
    date_paid = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_approved_invoices'


class TblAttendance(models.Model):
    tutor_name = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    tution_type = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_attendance'


class TblClaimSheet(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    normal_class = models.CharField(max_length=100)
    normal_time = models.CharField(max_length=100)
    normal_mark = models.CharField(max_length=100)
    normal_number = models.CharField(max_length=100)
    special_class = models.CharField(max_length=100)
    special_time = models.CharField(max_length=100)
    special_mark = models.CharField(max_length=100)
    special_number = models.CharField(max_length=100)
    onsite_class = models.CharField(max_length=100)
    onsite_time = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_claim_sheet'


class TblClearance(models.Model):
    name = models.CharField(max_length=100)
    enrollment_date = models.CharField(max_length=20)
    reason = models.CharField(max_length=100)
    bookshop = models.CharField(max_length=20)
    library = models.CharField(max_length=20)
    accounts = models.CharField(max_length=20)
    date_cleared = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_clearance'


class TblCrashCourseContract(models.Model):
    tutor_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    hours = models.IntegerField()
    time_duration = models.CharField(max_length=50)
    date_created = models.DateTimeField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tbl_crash_course_contract'


class TblEnglish(models.Model):
    first_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    issue_date = models.CharField(max_length=15)
    start_period = models.CharField(max_length=15)
    end_period = models.CharField(max_length=15)
    level = models.CharField(max_length=100)
    reading_cat = models.IntegerField()
    reading_progressive = models.IntegerField()
    reading_end = models.IntegerField()
    reading_total = models.IntegerField()
    reading_grade = models.CharField(max_length=10)
    writing_cat = models.IntegerField()
    writing_progressive = models.IntegerField()
    writing_end = models.IntegerField()
    writing_total = models.IntegerField()
    writing_grade = models.CharField(max_length=10)
    listening_cat = models.IntegerField()
    listening_progressive = models.IntegerField()
    listening_end = models.IntegerField()
    listening_total = models.IntegerField()
    listening_grade = models.CharField(max_length=10)
    speaking_cat = models.IntegerField()
    speaking_progressive = models.IntegerField()
    speaking_end = models.IntegerField()
    speaking_total = models.IntegerField()
    speaking_grade = models.CharField(max_length=10)
    grammar_cat = models.IntegerField()
    grammar_progressive = models.IntegerField()
    grammar_end = models.IntegerField()
    grammar_total = models.IntegerField()
    grammar_grade = models.CharField(max_length=10)
    entry_date = models.DateTimeField()
    average = models.IntegerField()
    accreditation = models.CharField(max_length=100)
    hours_attended = models.IntegerField()
    username = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    transcript_code = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_english'


class TblFiles(models.Model):
    username = models.CharField(max_length=50)
    recepient = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    filepath = models.CharField(max_length=100)
    read_status = models.CharField(max_length=50)
    sent_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_files'


class TblFrench(models.Model):
    first_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    issue_date = models.DateField()
    start_period = models.DateField()
    end_period = models.DateField()
    level = models.CharField(max_length=100)
    reading_cat = models.IntegerField()
    reading_progressive = models.IntegerField()
    reading_end = models.IntegerField()
    reading_total = models.IntegerField()
    reading_grade = models.CharField(max_length=10)
    writing_cat = models.IntegerField()
    writing_progressive = models.IntegerField()
    writing_end = models.IntegerField()
    writing_total = models.IntegerField()
    writing_grade = models.CharField(max_length=10)
    listening_cat = models.IntegerField()
    listening_progressive = models.IntegerField()
    listening_end = models.IntegerField()
    listening_total = models.IntegerField()
    listening_grade = models.CharField(max_length=10)
    speaking_cat = models.IntegerField()
    speaking_progressive = models.IntegerField()
    speaking_end = models.IntegerField()
    speaking_total = models.IntegerField()
    speaking_grade = models.CharField(max_length=10)
    grammar_cat = models.IntegerField()
    grammar_progressive = models.IntegerField()
    grammar_end = models.IntegerField()
    grammar_total = models.IntegerField()
    grammar_grade = models.CharField(max_length=10)
    entry_date = models.DateTimeField()
    average = models.IntegerField()
    accreditation = models.CharField(max_length=5)
    hours_attended = models.IntegerField()
    username = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_french'


class TblInquiries(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    interest = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    entry_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_inquiries'


class TblInventoryTransaction(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    issued_to = models.CharField(max_length=100)
    department_issued = models.CharField(max_length=100)
    quantity_issued = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_inventory_transaction'


class TblItalian(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    issue_date = models.DateField()
    start_period = models.DateField()
    end_period = models.DateField()
    level = models.CharField(max_length=100)
    reading_cat = models.IntegerField()
    reading_progressive = models.IntegerField()
    reading_end = models.IntegerField()
    reading_total = models.IntegerField()
    reading_grade = models.CharField(max_length=10)
    writing_cat = models.IntegerField()
    writing_progressive = models.IntegerField()
    writing_end = models.IntegerField()
    writing_total = models.IntegerField()
    writing_grade = models.CharField(max_length=10)
    listening_cat = models.IntegerField()
    listening_progressive = models.IntegerField()
    listening_end = models.IntegerField()
    listening_total = models.IntegerField()
    listening_grade = models.CharField(max_length=10)
    speaking_cat = models.IntegerField()
    speaking_progressive = models.IntegerField()
    speaking_end = models.IntegerField()
    speaking_total = models.IntegerField()
    speaking_grade = models.CharField(max_length=10)
    grammar_cat = models.IntegerField()
    grammar_progressive = models.IntegerField()
    grammar_end = models.IntegerField()
    grammar_total = models.IntegerField()
    grammar_grade = models.CharField(max_length=10)
    entry_date = models.DateTimeField()
    average = models.IntegerField()
    accreditation = models.CharField(max_length=5)
    hours_attended = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_italian'


class TblKiswahili(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    issue_date = models.DateField()
    start_period = models.DateField()
    end_period = models.DateField()
    level = models.CharField(max_length=100)
    reading_cat = models.IntegerField()
    reading_progressive = models.IntegerField()
    reading_end = models.IntegerField()
    reading_total = models.IntegerField()
    reading_grade = models.CharField(max_length=10)
    writing_cat = models.IntegerField()
    writing_progressive = models.IntegerField()
    writing_end = models.IntegerField()
    writing_total = models.IntegerField()
    writing_grade = models.CharField(max_length=10)
    listening_cat = models.IntegerField()
    listening_progressive = models.IntegerField()
    listening_end = models.IntegerField()
    listening_total = models.IntegerField()
    listening_grade = models.CharField(max_length=10)
    speaking_cat = models.IntegerField()
    speaking_progressive = models.IntegerField()
    speaking_end = models.IntegerField()
    speaking_total = models.IntegerField()
    speaking_grade = models.CharField(max_length=10)
    grammar_cat = models.IntegerField()
    grammar_progressive = models.IntegerField()
    grammar_end = models.IntegerField()
    grammar_total = models.IntegerField()
    grammar_grade = models.CharField(max_length=10)
    entry_date = models.DateTimeField()
    average = models.IntegerField()
    accreditation = models.CharField(max_length=5)
    hours_attended = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_kiswahili'


class TblLibrary(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    item1 = models.CharField(max_length=100)
    item2 = models.CharField(max_length=100)
    item3 = models.CharField(max_length=100)
    item4 = models.CharField(max_length=100)
    item5 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_library'


class TblLibraryClearance(models.Model):
    name = models.CharField(max_length=100)
    item_name1 = models.CharField(max_length=100)
    item_name2 = models.CharField(max_length=100)
    item_name3 = models.CharField(max_length=100)
    item_name4 = models.CharField(max_length=100)
    item_name5 = models.CharField(max_length=100)
    item_name6 = models.CharField(max_length=100)
    author_name1 = models.CharField(max_length=100)
    author_name2 = models.CharField(max_length=100)
    author_name3 = models.CharField(max_length=100)
    author_name4 = models.CharField(max_length=100)
    author_name5 = models.CharField(max_length=100)
    author_name6 = models.CharField(max_length=100)
    author_name7 = models.CharField(max_length=100)
    author_name8 = models.CharField(max_length=100)
    author_name9 = models.CharField(max_length=100)
    description1 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=100)
    description4 = models.CharField(max_length=100)
    description5 = models.CharField(max_length=100)
    description6 = models.CharField(max_length=100)
    description7 = models.CharField(max_length=100)
    description8 = models.CharField(max_length=100)
    description9 = models.CharField(max_length=100)
    quantity1 = models.CharField(max_length=10)
    quantity2 = models.CharField(max_length=10)
    quantity3 = models.CharField(max_length=10)
    quantity4 = models.CharField(max_length=10)
    quantity5 = models.CharField(max_length=10)
    quantity6 = models.CharField(max_length=10)
    quantity7 = models.CharField(max_length=10)
    quantity8 = models.CharField(max_length=10)
    quantity9 = models.CharField(max_length=10)
    submission_date = models.DateTimeField()
    clearance_status = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'tbl_library_clearance'


class TblLoginLogs(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    date_accessed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_login_logs'


class TblOnsiteContract(models.Model):
    tutor_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    hours = models.IntegerField()
    time_duration = models.CharField(max_length=50)
    date_created = models.DateTimeField()
    site = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tbl_onsite_contract'


class TblOthers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    issue_date = models.DateField()
    start_period = models.DateField()
    end_period = models.DateField()
    level = models.CharField(max_length=100)
    reading_cat = models.IntegerField()
    reading_progressive = models.IntegerField()
    reading_end = models.IntegerField()
    reading_total = models.IntegerField()
    reading_grade = models.CharField(max_length=10)
    writing_cat = models.IntegerField()
    writing_progressive = models.IntegerField()
    writing_end = models.IntegerField()
    writing_total = models.IntegerField()
    writing_grade = models.CharField(max_length=10)
    listening_cat = models.IntegerField()
    listening_progressive = models.IntegerField()
    listening_end = models.IntegerField()
    listening_total = models.IntegerField()
    listening_grade = models.CharField(max_length=10)
    speaking_cat = models.IntegerField()
    speaking_progressive = models.IntegerField()
    speaking_end = models.IntegerField()
    speaking_total = models.IntegerField()
    speaking_grade = models.CharField(max_length=10)
    grammar_cat = models.IntegerField()
    grammar_progressive = models.IntegerField()
    grammar_end = models.IntegerField()
    grammar_total = models.IntegerField()
    grammar_grade = models.CharField(max_length=10)
    entry_date = models.DateTimeField()
    average = models.IntegerField()
    accreditation = models.CharField(max_length=5)
    hours_attended = models.IntegerField()
    other_subjects = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_others'


class TblPortugese(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    issue_date = models.DateField()
    start_period = models.DateField()
    end_period = models.DateField()
    level = models.CharField(max_length=100)
    reading_cat = models.IntegerField()
    reading_progressive = models.IntegerField()
    reading_end = models.IntegerField()
    reading_total = models.IntegerField()
    reading_grade = models.CharField(max_length=10)
    writing_cat = models.IntegerField()
    writing_progressive = models.IntegerField()
    writing_end = models.IntegerField()
    writing_total = models.IntegerField()
    writing_grade = models.CharField(max_length=10)
    listening_cat = models.IntegerField()
    listening_progressive = models.IntegerField()
    listening_end = models.IntegerField()
    listening_total = models.IntegerField()
    listening_grade = models.CharField(max_length=10)
    speaking_cat = models.IntegerField()
    speaking_progressive = models.IntegerField()
    speaking_end = models.IntegerField()
    speaking_total = models.IntegerField()
    speaking_grade = models.CharField(max_length=10)
    grammar_cat = models.IntegerField()
    grammar_progressive = models.IntegerField()
    grammar_end = models.IntegerField()
    grammar_total = models.IntegerField()
    grammar_grade = models.CharField(max_length=10)
    entry_date = models.DateTimeField()
    average = models.IntegerField()
    accreditation = models.CharField(max_length=5)
    hours_attended = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_portugese'


class TblPriceList(models.Model):
    item = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    production_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tbl_price_list'


class TblQrcodes(models.Model):
    transcript_code = models.CharField(max_length=100)
    qrimage = models.CharField(max_length=100)
    prepared_by = models.CharField(max_length=100)
    issued_by = models.CharField(max_length=100)
    date_issued = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_qrcodes'


class TblRecordSlip(models.Model):
    invoiceid = models.AutoField(db_column='invoiceID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_description = models.CharField(max_length=100)
    language_from = models.CharField(max_length=50)
    language_to = models.CharField(max_length=50)
    start_date = models.DateField()
    interpretation_hours = models.IntegerField()
    total_interpretation = models.IntegerField()
    proof_read_words = models.IntegerField()
    proof_read_total = models.IntegerField()
    translated_words = models.IntegerField()
    translated_total = models.IntegerField()
    transcription_hours = models.IntegerField()
    transcription_total = models.IntegerField()
    forty_translation = models.IntegerField()
    forty_proof_reading = models.IntegerField()
    forty_interpretation = models.IntegerField()
    forty_transcription = models.IntegerField()
    sixty_translation = models.IntegerField()
    sixty_proof_reading = models.IntegerField()
    sixty_interpretation = models.IntegerField()
    sixty_transcription = models.IntegerField()
    stamp_seal_translation = models.IntegerField()
    stamp_seal_proof_reading = models.IntegerField()
    sub_total_translation = models.IntegerField()
    sub_total_proof_reading = models.IntegerField()
    sub_total_interpretation = models.IntegerField()
    sub_total_transcription = models.IntegerField()
    total_forty_percent = models.IntegerField()
    total_sixty_percent = models.IntegerField()
    level_of_education = models.CharField(max_length=100)
    tuition_amount = models.CharField(max_length=100)
    tuition_hours = models.CharField(max_length=100)
    tuition_total_paid = models.CharField(max_length=100)
    software_service_total = models.CharField(max_length=100)
    ies_total = models.CharField(max_length=100)
    grand_total_ksh = models.IntegerField()
    month = models.CharField(max_length=30)
    payment_status = models.CharField(max_length=10)
    service_payment_status = models.CharField(max_length=10)
    slip_no = models.IntegerField()
    year = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tbl_record_slip'


class TblResults(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    issue_date = models.DateField()
    start_period = models.DateField()
    end_period = models.DateField()
    level = models.CharField(max_length=250)
    introduction_cat = models.IntegerField()
    introduction_progressive = models.IntegerField()
    introduction_end = models.IntegerField()
    introduction_total = models.IntegerField()
    introduction_grade = models.CharField(max_length=11)
    windows_cat = models.IntegerField()
    windows_progressive = models.IntegerField()
    windows_end = models.IntegerField()
    windows_total = models.IntegerField()
    windows_grade = models.CharField(max_length=11)
    word_cat = models.IntegerField()
    word_progressive = models.IntegerField()
    word_end = models.IntegerField()
    word_total = models.IntegerField()
    word_grade = models.CharField(max_length=11)
    excel_cat = models.IntegerField()
    excel_progressive = models.IntegerField()
    excel_end = models.IntegerField()
    excel_total = models.IntegerField()
    excel_grade = models.CharField(max_length=11)
    access_cat = models.IntegerField()
    access_progressive = models.IntegerField()
    access_end = models.IntegerField()
    access_total = models.IntegerField()
    access_grade = models.CharField(max_length=11)
    powerpoint_cat = models.IntegerField()
    powerpoint_progressive = models.IntegerField()
    powerpoint_end = models.IntegerField()
    powerpoint_total = models.IntegerField()
    powerpoint_grade = models.CharField(max_length=11)
    publisher_cat = models.IntegerField()
    publisher_progressive = models.IntegerField()
    publisher_end = models.IntegerField()
    publisher_total = models.IntegerField()
    publisher_grade = models.CharField(max_length=11)
    dos_cat = models.IntegerField()
    dos_progressive = models.IntegerField()
    dos_end = models.IntegerField()
    dos_total = models.IntegerField()
    dos_grade = models.CharField(max_length=11)
    internet_cat = models.IntegerField()
    internet_progressive = models.IntegerField()
    internet_end = models.IntegerField()
    internet_total = models.IntegerField()
    internet_grade = models.CharField(max_length=11)
    photoshop_cat = models.IntegerField()
    photoshop_progressive = models.IntegerField()
    photoshop_end = models.IntegerField()
    photoshop_total = models.IntegerField()
    photoshop_grade = models.CharField(max_length=11)
    networking_cat = models.IntegerField()
    networking_progressive = models.IntegerField()
    networking_end = models.IntegerField()
    networking_total = models.IntegerField()
    networking_grade = models.CharField(max_length=11)
    keyboarding_cat = models.IntegerField()
    keyboarding_progressive = models.IntegerField()
    keyboarding_end = models.IntegerField()
    keyboarding_total = models.IntegerField()
    keyboarding_grade = models.CharField(max_length=11)
    entry_date = models.DateTimeField()
    average = models.IntegerField()
    accreditation = models.CharField(max_length=5)
    hours_attended = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_results'


class TblSchoolInvoice(models.Model):
    invoiceid = models.AutoField(db_column='invoiceID', primary_key=True)  # Field name made lowercase.
    invoice_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=100)
    billing_self = models.CharField(max_length=100)
    issue_date = models.DateField()
    due_date = models.DateField()
    language_category = models.CharField(max_length=20)
    language_checkbox = models.CharField(max_length=100)
    computer_category = models.CharField(max_length=20)
    computer_checkbox = models.CharField(max_length=50)
    languages = models.CharField(max_length=20)
    level = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    dollar_rate = models.IntegerField()
    euro_rate = models.IntegerField()
    previous_balance = models.IntegerField()
    balance_ksh_total = models.IntegerField()
    balance_dollar_total = models.IntegerField()
    balance_euro_total = models.IntegerField()
    language_hours = models.IntegerField()
    language_ksh_total = models.IntegerField()
    language_dollar_total = models.IntegerField()
    language_euro_total = models.IntegerField()
    registration_amount = models.IntegerField()
    registration_ksh_total = models.IntegerField()
    registration_dollar_total = models.IntegerField()
    registration_euro_total = models.IntegerField()
    text_book_number = models.IntegerField()
    text_book_amount = models.IntegerField()
    text_book_ksh_total = models.IntegerField()
    text_book_dollar_total = models.IntegerField()
    text_book_euro_total = models.IntegerField()
    activity_fee_amount = models.IntegerField()
    activity_fee_ksh_total = models.IntegerField()
    activity_fee_dollar_total = models.IntegerField()
    activity_fee_euro_total = models.IntegerField()
    id_card_amount = models.IntegerField()
    id_card_ksh_total = models.IntegerField()
    id_card_dollar_total = models.IntegerField()
    id_card_euro_total = models.IntegerField()
    ict_hours = models.IntegerField()
    ict_ksh_total = models.IntegerField()
    ict_dollar_total = models.IntegerField()
    ict_euro_total = models.IntegerField()
    interpretation_hours = models.IntegerField()
    interpretation_amount = models.IntegerField()
    interpretation_ksh_total = models.IntegerField()
    interpretation_dollar_total = models.IntegerField()
    interpretation_euro_total = models.IntegerField()
    translation_hours = models.IntegerField()
    translation_amount = models.IntegerField()
    translation_ksh_total = models.IntegerField()
    translation_dollar_total = models.IntegerField()
    translation_euro_total = models.IntegerField()
    grand_total_ksh_total = models.IntegerField()
    grand_total_dollar_total = models.IntegerField()
    grand_total_euro_total = models.IntegerField()
    discount_amount = models.IntegerField()
    discount_ksh_total = models.IntegerField()
    discount_dollar_total = models.IntegerField()
    discount_euro_total = models.IntegerField()
    effected_payment_amount = models.IntegerField()
    effected_payment_ksh_total = models.IntegerField()
    effected_payment_dollar_total = models.IntegerField()
    effected_payment_euro_total = models.IntegerField()
    overall_balance_ksh_total = models.IntegerField()
    overall_balance_dollar_total = models.IntegerField()
    overall_balance_euro_total = models.IntegerField()
    month = models.CharField(max_length=30)
    invoice_number1 = models.IntegerField()
    payment_status = models.CharField(max_length=10)
    year = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tbl_school_invoice'


class TblSpanish(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    issue_date = models.DateField()
    start_period = models.DateField()
    end_period = models.DateField()
    level = models.CharField(max_length=100)
    reading_cat = models.IntegerField()
    reading_progressive = models.IntegerField()
    reading_end = models.IntegerField()
    reading_total = models.IntegerField()
    reading_grade = models.CharField(max_length=10)
    writing_cat = models.IntegerField()
    writing_progressive = models.IntegerField()
    writing_end = models.IntegerField()
    writing_total = models.IntegerField()
    writing_grade = models.CharField(max_length=10)
    listening_cat = models.IntegerField()
    listening_progressive = models.IntegerField()
    listening_end = models.IntegerField()
    listening_total = models.IntegerField()
    listening_grade = models.CharField(max_length=10)
    speaking_cat = models.IntegerField()
    speaking_progressive = models.IntegerField()
    speaking_end = models.IntegerField()
    speaking_total = models.IntegerField()
    speaking_grade = models.CharField(max_length=10)
    grammar_cat = models.IntegerField()
    grammar_progressive = models.IntegerField()
    grammar_end = models.IntegerField()
    grammar_total = models.IntegerField()
    grammar_grade = models.CharField(max_length=10)
    entry_date = models.DateTimeField()
    average = models.IntegerField()
    accreditation = models.CharField(max_length=5)
    hours_attended = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_spanish'


class TblStudents(models.Model):
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    form = models.CharField(max_length=255)
    father_phone = models.CharField(max_length=255)
    mother_phone = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    activation_code = models.CharField(db_column='Activation_Code', max_length=255)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=1)  # Field name made lowercase.
    admin = models.CharField(max_length=20)
    time_registered = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_students'



class TblSubscription(models.Model):
    registration_date = models.CharField(max_length=11)
    expiry_date = models.CharField(max_length=20)
    activated_days = models.CharField(max_length=5)
    status = models.CharField(max_length=11)
    activation_code = models.CharField(max_length=20)
    vendor_code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tbl_subscription'


class TblSuperAdmin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_super_admin'


class TblTeachers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comment = models.CharField(max_length=100)
    gender = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    paper = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    activation_code = models.CharField(db_column='Activation_Code', max_length=255)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=1)  # Field name made lowercase.
    admin = models.CharField(max_length=20)
    paper_assigned = models.CharField(max_length=255)
    time_registered = models.DateTimeField()
    education_rate = models.IntegerField()
    salaries = models.IntegerField()
    education_level = models.CharField(max_length=20)
    registration_date = models.CharField(max_length=50)
    moment_date = models.CharField(max_length=50)
    expiry_date = models.CharField(max_length=50)
    activated_days = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    activation_codes = models.CharField(max_length=50)
    vendor_code = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_teachers'


class TblTeachersPay(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    course = models.CharField(max_length=20)
    education = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    normal_mark1 = models.CharField(max_length=5)
    normal_mark2 = models.CharField(max_length=5)
    special_mark = models.CharField(max_length=5)
    number_normal = models.IntegerField()
    special_number = models.IntegerField()
    onsite_mark = models.CharField(max_length=5)
    onsite_number = models.IntegerField()
    normal_class_hours = models.IntegerField()
    normal_class_total = models.IntegerField()
    afternoon_activity_rate = models.IntegerField()
    activities_hours = models.IntegerField()
    activities_total = models.IntegerField()
    quality_work_rate = models.IntegerField()
    tod_hours = models.IntegerField()
    tod_total = models.IntegerField()
    special_class_rate = models.IntegerField()
    tutored_hours = models.IntegerField()
    tutored_total = models.IntegerField()
    eca_rate = models.IntegerField()
    eca_hours = models.IntegerField()
    eca_total = models.IntegerField()
    meeting_rate = models.IntegerField()
    meeting_number = models.IntegerField()
    meeting_total = models.IntegerField()
    placement_rate = models.IntegerField()
    test_number = models.IntegerField()
    test_total = models.IntegerField()
    internet_total = models.IntegerField()
    normal_class2_rate = models.IntegerField()
    normal2_hours = models.IntegerField()
    normal2_total = models.IntegerField()
    onsite_rate = models.IntegerField()
    onsite_hours = models.IntegerField()
    onsite_total = models.IntegerField()
    salaries = models.IntegerField()
    summation1 = models.IntegerField()
    advance = models.IntegerField()
    advance_total = models.IntegerField()
    charity = models.IntegerField()
    charity_total = models.IntegerField()
    others = models.IntegerField()
    others_total = models.IntegerField()
    summation2 = models.IntegerField()
    gross_total = models.IntegerField()
    date_submitted = models.DateTimeField()
    payment_status = models.CharField(max_length=10)
    approval_status = models.CharField(max_length=50)
    year = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'tbl_teachers_pay'


class TblTransactions(models.Model):
    name = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    payment_code = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_transactions'
