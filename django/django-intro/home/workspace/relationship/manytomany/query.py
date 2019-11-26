# 1. 생성
doctor1 = Doctor.objects.create(name='Kim')
doctor2 = Doctor.objects.create(name='Park')
patient1 = Patient.objects.create(name='Tom')
patient2 = Patient.objects.create(name='John')
Reservation.objects.create(doctor=doctor1, patient=patient1)
Reservation.objects.create(doctor=doctor1, patient=patient2)
Reservation.objects.create(doctor=doctor2, patient=patient1)
# 2. 의사 1의 예약 목록
doctor = Doctor.objects.get(pk=1)
doctor.reservation_set.all()
# Reservation.objects.filter(doctor=doctor)
# 3. 의사 1의 환자의 이름
doctor = Doctor.objects.get(pk=1)
reservations = doctor.reservation_set.all()
for r in reservations:
    print(r.patient.name)
    
# =================================================================
# 1. Patient에 doctors = ManyToManyField(Doctor, through='Reservation')
patient = Patient.objects.get(pk=1)
patient.doctors.all()
doctor = Doctor.objects.get(pk=1)
doctor.patient_set.all()

# 2. Patient에 doctors = ManyToManyField(Doctor, through='Reservation', related_name='patients')
# 역참조와 관련된 설정을 한다면
patient = Patient.objects.get(pk=1)
patient.doctors.all()
doctor = Doctor.objects.get(pk=1)
doctor.patients.all()

# 3. 예약 생성
Reservation(patient=patient, doctor=doctor)

# ================================================================
# 1. 중개모델이 없다면,
patient = Patient.objects.get(pk=1)
patient.doctors.all()
doctor = Doctor.objects.get(pk=1)
doctor.patients.all()

# 2. 예약을 생성한다면,
patient = Patient.objects.get(pk=1)
doctor = Doctor.objects.get(pk=1)
patient.doctors.add(doctor)
# 혹은
doctor.patients.add(patient)