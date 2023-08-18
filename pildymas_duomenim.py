from model import Customer, Order_, sessionmaker, engine

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = input('Pasirinkite veiksmą:\n1. Pirkėjų administravimas\n2. Prekių administravimas\n'
                         '3. Vartotojo menu\n4. Išeiti iš programos')
    while True:
        if pasirinkimas == '1':
            administravimas1 = input('1. Įveskite pirkėją\n2. Redaguokite pirkėją.\n'
                                     '3. Pašalinkite pirkėją\n4. Perziureti pirkejus\n5. Pagrindinis menu')
            if administravimas1 == '1':
                vardas = input('Iveskite vardas\n')
                pavarde = input('Iveskite pavarde\n')
                email = input('Iveskite emaila\n')
                customer_o = Customer(f_name=f'{vardas}', l_name=f'{pavarde}', email=f'{email}')
                session.add(customer_o)
            session.commit()
            if administravimas1 == '2':
                redagavimas1 = input('Iveskite redaguojamo pirkejo varda')
                redagavimas2 = input('Iveskite  nauja varda')
                # obj_red = session.query(Customer).filter(Customer.f_name.ilike(f"{redagavimas1}%")).one()
                # customer_o.f_name = redagavimas2
                # session.commit()
            if administravimas1 == '3':
                trinamas = input('Iveskite trinamo pirkejo varda')
                obj_del = session.query(Customer).filter(Customer.f_name.ilike(f"{trinamas}%")).one()
                session.delete(obj_del)
                session.commit()
            if administravimas1 == '4':
                eil_objs = session.query(Customer).all()
                for eil_o in eil_objs:
                    print(eil_o.f_name, eil_o.l_name, eil_o.email)
            if administravimas1 == '5':
                break
            continue