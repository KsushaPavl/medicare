# JSON-LD blocks for medicare-radom.pl

Insert each block inside `<head>`, just before the closing `</head>` tag.
Multiple `<script type="application/ld+json">` blocks on one page are valid.

The clinic block repeats on every page. This is intentional, not a duplicate:
the shared `@id` merges them into a single entity.

Verify before publishing:

- `name` must match the clinic name in Google Business Profile
- FAQ answers must match the visible page text word for word
- prices appear both in the HTML table and here; update both when they change

---

## index.html

2 blocks.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "@id": "https://medicare-radom.pl/#clinic",
  "name": "Przychodnia MediCare",
  "description": "Wielospecjalistyczna przychodnia w Radomiu. Kardiolog, chirurg, neurolog, USG, RTG i Holter EKG.",
  "url": "https://medicare-radom.pl/",
  "logo": "https://medicare-radom.pl/assets/logo.png",
  "image": "https://medicare-radom.pl/assets/building.jpg",
  "telephone": "+48889834936",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "ul. Dębowa 2",
    "addressLocality": "Radom",
    "postalCode": "26-610",
    "addressCountry": "PL"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 51.3970839,
    "longitude": 21.1353775
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "08:00",
    "closes": "18:00"
  }],
  "sameAs": [
    "https://www.facebook.com/profile.php?id=61579875898421",
    "https://www.instagram.com/przychodnia_medicare/",
    "https://www.znanylekarz.pl/placowki/przychodnia-medicare-3"
  ],
  "medicalSpecialty": [
    "Cardiovascular",
    "Otolaryngologic",
    "Urologic",
    "Renal",
    "Neurologic",
    "Rheumatologic",
    "Psychiatric",
    "Surgical",
    "PlasticSurgery",
    "Radiography"
  ],
  "availableService": [
    { "@type": "MedicalTest", "name": "USG" },
    { "@type": "MedicalTest", "name": "RTG" },
    { "@type": "MedicalTest", "name": "Holter EKG" }
  ],
  "isAcceptingNewPatients": true,
  "hasMap": "https://maps.google.com/?q=ul.+D%C4%99bowa+2,+26-610+Radom"
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://medicare-radom.pl/#website",
  "name": "Przychodnia MediCare",
  "url": "https://medicare-radom.pl/",
  "inLanguage": "pl-PL",
  "publisher": { "@id": "https://medicare-radom.pl/#clinic" }
}
</script>
```

---

## przychodnia.html

3 blocks.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "@id": "https://medicare-radom.pl/#clinic",
  "name": "Przychodnia MediCare",
  "description": "Wielospecjalistyczna przychodnia w Radomiu. Kardiolog, chirurg, neurolog, USG, RTG i Holter EKG.",
  "url": "https://medicare-radom.pl/",
  "logo": "https://medicare-radom.pl/assets/logo.png",
  "image": "https://medicare-radom.pl/assets/building.jpg",
  "telephone": "+48889834936",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "ul. Dębowa 2",
    "addressLocality": "Radom",
    "postalCode": "26-610",
    "addressCountry": "PL"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 51.3970839,
    "longitude": 21.1353775
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "08:00",
    "closes": "18:00"
  }],
  "sameAs": [
    "https://www.facebook.com/profile.php?id=61579875898421",
    "https://www.instagram.com/przychodnia_medicare/",
    "https://www.znanylekarz.pl/placowki/przychodnia-medicare-3"
  ],
  "medicalSpecialty": [
    "Cardiovascular",
    "Otolaryngologic",
    "Urologic",
    "Renal",
    "Neurologic",
    "Rheumatologic",
    "Psychiatric",
    "Surgical",
    "PlasticSurgery",
    "Radiography"
  ],
  "availableService": [
    { "@type": "MedicalTest", "name": "USG" },
    { "@type": "MedicalTest", "name": "RTG" },
    { "@type": "MedicalTest", "name": "Holter EKG" }
  ],
  "isAcceptingNewPatients": true,
  "hasMap": "https://maps.google.com/?q=ul.+D%C4%99bowa+2,+26-610+Radom"
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Strona główna", "item": "https://medicare-radom.pl/" },
    { "@type": "ListItem", "position": 2, "name": "O nas", "item": "https://medicare-radom.pl/przychodnia.html" }
  ]
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "O nas – Przychodnia MediCare Radom",
  "url": "https://medicare-radom.pl/przychodnia.html",
  "inLanguage": "pl-PL",
  "description": "Wielospecjalistyczna przychodnia przy ul. Dębowej 2 w Radomiu. Nowoczesny budynek dostosowany dla osób niepełnosprawnych, diagnostyka RTG i USG na miejscu, kilkanaście specjalizacji medycznych.",
  "mainEntity": { "@id": "https://medicare-radom.pl/#clinic" }
}
</script>
```

---

## poradnie.html

4 blocks.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "@id": "https://medicare-radom.pl/#clinic",
  "name": "Przychodnia MediCare",
  "description": "Wielospecjalistyczna przychodnia w Radomiu. Kardiolog, chirurg, neurolog, USG, RTG i Holter EKG.",
  "url": "https://medicare-radom.pl/",
  "logo": "https://medicare-radom.pl/assets/logo.png",
  "image": "https://medicare-radom.pl/assets/building.jpg",
  "telephone": "+48889834936",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "ul. Dębowa 2",
    "addressLocality": "Radom",
    "postalCode": "26-610",
    "addressCountry": "PL"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 51.3970839,
    "longitude": 21.1353775
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "08:00",
    "closes": "18:00"
  }],
  "sameAs": [
    "https://www.facebook.com/profile.php?id=61579875898421",
    "https://www.instagram.com/przychodnia_medicare/",
    "https://www.znanylekarz.pl/placowki/przychodnia-medicare-3"
  ],
  "medicalSpecialty": [
    "Cardiovascular",
    "Otolaryngologic",
    "Urologic",
    "Renal",
    "Neurologic",
    "Rheumatologic",
    "Psychiatric",
    "Surgical",
    "PlasticSurgery",
    "Radiography"
  ],
  "availableService": [
    { "@type": "MedicalTest", "name": "USG" },
    { "@type": "MedicalTest", "name": "RTG" },
    { "@type": "MedicalTest", "name": "Holter EKG" }
  ],
  "isAcceptingNewPatients": true,
  "hasMap": "https://maps.google.com/?q=ul.+D%C4%99bowa+2,+26-610+Radom"
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Strona główna", "item": "https://medicare-radom.pl/" },
    { "@type": "ListItem", "position": 2, "name": "Poradnie", "item": "https://medicare-radom.pl/poradnie.html" }
  ]
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Poradnie – Przychodnia MediCare Radom",
  "url": "https://medicare-radom.pl/poradnie.html",
  "inLanguage": "pl-PL",
  "about": { "@id": "https://medicare-radom.pl/#clinic" },
  "mainEntity": {
    "@type": "ItemList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Poradnia Chirurgii Ogólnej i Proktologii" },
      { "@type": "ListItem", "position": 2, "name": "Poradnia Leczenia Ran" },
      { "@type": "ListItem", "position": 3, "name": "Poradnia Zdrowia Psychicznego" },
      { "@type": "ListItem", "position": 4, "name": "Poradnia Chirurgii Plastycznej" },
      { "@type": "ListItem", "position": 5, "name": "Poradnia Kardiologiczna" },
      { "@type": "ListItem", "position": 6, "name": "Poradnia Chirurgii Naczyniowej" },
      { "@type": "ListItem", "position": 7, "name": "Poradnia Urologiczna" },
      { "@type": "ListItem", "position": 8, "name": "Poradnia Nefrologiczna" },
      { "@type": "ListItem", "position": 9, "name": "Poradnia Neurologiczna" },
      { "@type": "ListItem", "position": 10, "name": "Poradnia Reumatologiczna" },
      { "@type": "ListItem", "position": 11, "name": "Poradnia Otolaryngologiczna" },
      { "@type": "ListItem", "position": 12, "name": "Poradnia Chorób Wewnętrznych" }
    ]
  }
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Person", "name": "Piotr Kluska", "honorificPrefix": "dr n. med.", "jobTitle": "Specjalista chirurgii ogólnej, proktolog", "worksFor": { "@id": "https://medicare-radom.pl/#clinic" } },
    { "@type": "Person", "name": "Paulina Szymańska", "honorificPrefix": "dr n. o zdr.", "jobTitle": "Specjalista leczenia ran", "worksFor": { "@id": "https://medicare-radom.pl/#clinic" } },
    { "@type": "Person", "name": "Tomasz Golański", "honorificPrefix": "lek.", "jobTitle": "Specjalista psychiatrii", "worksFor": { "@id": "https://medicare-radom.pl/#clinic" } },
    { "@type": "Person", "name": "Raman Paulouski", "honorificPrefix": "lek.", "jobTitle": "Chirurg", "worksFor": { "@id": "https://medicare-radom.pl/#clinic" } },
    { "@type": "Person", "name": "Eliza Słodka", "honorificPrefix": "lek.", "jobTitle": "Specjalista kardiologii, specjalista chorób wewnętrznych", "worksFor": { "@id": "https://medicare-radom.pl/#clinic" } },
    { "@type": "Person", "name": "Robert Kapołka", "honorificPrefix": "lek.", "jobTitle": "Specjalista chirurgii naczyniowej", "worksFor": { "@id": "https://medicare-radom.pl/#clinic" } },
    { "@type": "Person", "name": "Mikołaj Ostrach", "honorificPrefix": "lek.", "jobTitle": "Specjalista urologii", "worksFor": { "@id": "https://medicare-radom.pl/#clinic" } },
    { "@type": "Person", "name": "Łukasz Skórka", "honorificPrefix": "lek.", "jobTitle": "Specjalista nefrologii, specjalista chorób wewnętrznych", "worksFor": { "@id": "https://medicare-radom.pl/#clinic" } },
    { "@type": "Person", "name": "Anna Narożnik", "honorificPrefix": "lek.", "jobTitle": "Specjalista neurologii", "worksFor": { "@id": "https://medicare-radom.pl/#clinic" } },
    { "@type": "Person", "name": "Agata Skwarek-Szewczyk", "honorificPrefix": "lek.", "jobTitle": "Specjalista reumatologii, specjalista chorób wewnętrznych", "worksFor": { "@id": "https://medicare-radom.pl/#clinic" } },
    { "@type": "Person", "name": "Paulina Zarębska-Karpieszuk", "honorificPrefix": "dr n. med.", "jobTitle": "Specjalista otolaryngologii", "worksFor": { "@id": "https://medicare-radom.pl/#clinic" } },
    { "@type": "Person", "name": "Wojciech Rogozik", "honorificPrefix": "lek.", "jobTitle": "Specjalista otolaryngologii", "worksFor": { "@id": "https://medicare-radom.pl/#clinic" } }
  ]
}
</script>
```

---

## cennik.html

3 blocks.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "@id": "https://medicare-radom.pl/#clinic",
  "name": "Przychodnia MediCare",
  "description": "Wielospecjalistyczna przychodnia w Radomiu. Kardiolog, chirurg, neurolog, USG, RTG i Holter EKG.",
  "url": "https://medicare-radom.pl/",
  "logo": "https://medicare-radom.pl/assets/logo.png",
  "image": "https://medicare-radom.pl/assets/building.jpg",
  "telephone": "+48889834936",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "ul. Dębowa 2",
    "addressLocality": "Radom",
    "postalCode": "26-610",
    "addressCountry": "PL"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 51.3970839,
    "longitude": 21.1353775
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "08:00",
    "closes": "18:00"
  }],
  "sameAs": [
    "https://www.facebook.com/profile.php?id=61579875898421",
    "https://www.instagram.com/przychodnia_medicare/",
    "https://www.znanylekarz.pl/placowki/przychodnia-medicare-3"
  ],
  "medicalSpecialty": [
    "Cardiovascular",
    "Otolaryngologic",
    "Urologic",
    "Renal",
    "Neurologic",
    "Rheumatologic",
    "Psychiatric",
    "Surgical",
    "PlasticSurgery",
    "Radiography"
  ],
  "availableService": [
    { "@type": "MedicalTest", "name": "USG" },
    { "@type": "MedicalTest", "name": "RTG" },
    { "@type": "MedicalTest", "name": "Holter EKG" }
  ],
  "isAcceptingNewPatients": true,
  "hasMap": "https://maps.google.com/?q=ul.+D%C4%99bowa+2,+26-610+Radom"
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Strona główna", "item": "https://medicare-radom.pl/" },
    { "@type": "ListItem", "position": 2, "name": "Usługi i cennik", "item": "https://medicare-radom.pl/cennik.html" }
  ]
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "@id": "https://medicare-radom.pl/#clinic",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Cennik usług",
    "itemListElement": [
      {
        "@type": "OfferCatalog",
        "name": "Poradnia Chirurgii Ogólnej i Proktologii",
        "itemListElement": [
          { "@type": "Offer", "name": "Konsultacja chirurgiczna", "price": "300", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Konsultacja z badaniem dermatoskopowym", "price": "350", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Konsultacja proktologiczna", "price": "300", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Konsultacja proktologiczna z anoskopią", "price": "380", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Amputacja palca stopy", "price": "1200", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Plastyka wrastającego paznokcia", "price": "550", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Kontrola rany, zdjęcie szwów", "price": "100", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Wycięcie zmiany skórnej", "price": "500", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Wycięcie 3 zmian skórnych", "price": "700", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Badanie histopatologiczne", "price": "200", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Leczenie hemoroidów metodą Barrona", "price": "600", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Skleroterapia", "price": "1000", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Nacięcie zakrzepu brzeżnego", "price": "500", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Zabieg implantacji wszywki alkoholowej", "price": "700", "priceCurrency": "PLN" }
        ]
      },
      {
        "@type": "OfferCatalog",
        "name": "Poradnia Chirurgii Plastycznej",
        "itemListElement": [
          { "@type": "Offer", "name": "Kwalifikacja do zabiegu blefaroplastyki", "price": "200", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Plastyka powiek dolnych", "price": "4000", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Plastyka powiek górnych", "price": "3600", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Brow Lift (lifting brwi)", "price": "3600", "priceCurrency": "PLN" }
        ]
      },
      {
        "@type": "OfferCatalog",
        "name": "Poradnia Leczenia Ran",
        "itemListElement": [
          { "@type": "Offer", "name": "Usunięcie modzeli", "price": "100", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Zdjęcie szwów, klamerek", "price": "100", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Terapia ran przewlekłych", "priceSpecification": { "@type": "PriceSpecification", "minPrice": "270", "priceCurrency": "PLN" } },
          { "@type": "Offer", "name": "Terapia podciśnieniowa NPWT", "price": "900", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Terapia larwami", "priceSpecification": { "@type": "PriceSpecification", "minPrice": "1000", "priceCurrency": "PLN" } },
          { "@type": "Offer", "name": "Terapia fibryną – opatrunek autologiczny", "priceSpecification": { "@type": "PriceSpecification", "minPrice": "550", "priceCurrency": "PLN" } },
          { "@type": "Offer", "name": "Opracowanie owrzodzeń obu kończyn dolnych", "price": "350", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Opatrunek z podtlenkiem azotu", "price": "400", "priceCurrency": "PLN" }
        ]
      },
      {
        "@type": "OfferCatalog",
        "name": "Poradnia Otolaryngologiczna",
        "itemListElement": [
          { "@type": "Offer", "name": "Konsultacja laryngologiczna", "price": "300", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Konsultacja laryngologiczna z nasofiberoskopią", "price": "400", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Endoskopia laryngologiczna", "price": "350", "priceCurrency": "PLN" }
        ]
      },
      {
        "@type": "OfferCatalog",
        "name": "Poradnia Kardiologiczna",
        "itemListElement": [
          { "@type": "Offer", "name": "Konsultacja kardiologiczna", "price": "300", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "ECHO serca", "price": "250", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Holter EKG", "price": "180", "priceCurrency": "PLN" }
        ]
      },
      {
        "@type": "OfferCatalog",
        "name": "Poradnia Chirurgii Naczyniowej",
        "itemListElement": [
          { "@type": "Offer", "name": "Konsultacja z USG doppler", "price": "450", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Konsultacja rany przewlekłej", "price": "250", "priceCurrency": "PLN" }
        ]
      },
      {
        "@type": "OfferCatalog",
        "name": "Poradnia Nefrologiczna",
        "itemListElement": [
          { "@type": "Offer", "name": "Konsultacja nefrologiczna", "price": "250", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Konsultacja nefrologiczna z USG", "price": "300", "priceCurrency": "PLN" }
        ]
      },
      {
        "@type": "OfferCatalog",
        "name": "Poradnia Urologiczna",
        "itemListElement": [
          { "@type": "Offer", "name": "Konsultacja urologiczna", "price": "250", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Konsultacja urologiczna z USG", "price": "300", "priceCurrency": "PLN" }
        ]
      },
      {
        "@type": "OfferCatalog",
        "name": "Poradnia Neurologiczna",
        "itemListElement": [
          { "@type": "Offer", "name": "Konsultacja neurologiczna", "price": "250", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Wizyta kontrolna", "price": "200", "priceCurrency": "PLN" }
        ]
      },
      {
        "@type": "OfferCatalog",
        "name": "Poradnia Reumatologiczna",
        "itemListElement": [
          { "@type": "Offer", "name": "Konsultacja reumatologiczna", "price": "300", "priceCurrency": "PLN" },
          { "@type": "Offer", "name": "Zdjęcie RTG", "price": "60", "priceCurrency": "PLN" }
        ]
      },
      {
        "@type": "OfferCatalog",
        "name": "Poradnia Zdrowia Psychicznego",
        "itemListElement": [
          { "@type": "Offer", "name": "Konsultacja psychiatryczna", "price": "250", "priceCurrency": "PLN" }
        ]
      }
    ]
  }
}
</script>
```

---

## blefaroplastyka.html

4 blocks.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "@id": "https://medicare-radom.pl/#clinic",
  "name": "Przychodnia MediCare",
  "description": "Wielospecjalistyczna przychodnia w Radomiu. Kardiolog, chirurg, neurolog, USG, RTG i Holter EKG.",
  "url": "https://medicare-radom.pl/",
  "logo": "https://medicare-radom.pl/assets/logo.png",
  "image": "https://medicare-radom.pl/assets/building.jpg",
  "telephone": "+48889834936",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "ul. Dębowa 2",
    "addressLocality": "Radom",
    "postalCode": "26-610",
    "addressCountry": "PL"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 51.3970839,
    "longitude": 21.1353775
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "08:00",
    "closes": "18:00"
  }],
  "sameAs": [
    "https://www.facebook.com/profile.php?id=61579875898421",
    "https://www.instagram.com/przychodnia_medicare/",
    "https://www.znanylekarz.pl/placowki/przychodnia-medicare-3"
  ],
  "medicalSpecialty": [
    "Cardiovascular",
    "Otolaryngologic",
    "Urologic",
    "Renal",
    "Neurologic",
    "Rheumatologic",
    "Psychiatric",
    "Surgical",
    "PlasticSurgery",
    "Radiography"
  ],
  "availableService": [
    { "@type": "MedicalTest", "name": "USG" },
    { "@type": "MedicalTest", "name": "RTG" },
    { "@type": "MedicalTest", "name": "Holter EKG" }
  ],
  "isAcceptingNewPatients": true,
  "hasMap": "https://maps.google.com/?q=ul.+D%C4%99bowa+2,+26-610+Radom"
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Strona główna", "item": "https://medicare-radom.pl/" },
    { "@type": "ListItem", "position": 2, "name": "Poradnie", "item": "https://medicare-radom.pl/poradnie.html" },
    { "@type": "ListItem", "position": 3, "name": "Blefaroplastyka", "item": "https://medicare-radom.pl/blefaroplastyka.html" }
  ]
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalWebPage",
  "name": "Blefaroplastyka – plastyka powiek w Radomiu",
  "url": "https://medicare-radom.pl/blefaroplastyka.html",
  "inLanguage": "pl-PL",
  "about": {
    "@type": "MedicalProcedure",
    "name": "Blefaroplastyka",
    "alternateName": "Plastyka powiek",
    "procedureType": "https://schema.org/SurgicalProcedure",
    "bodyLocation": "Powieki",
    "howPerformed": "Zabieg wykonywany w znieczuleniu miejscowym, trwa 60–90 minut. Cięcia prowadzone są w naturalnym załamaniu powieki. Szwy zdejmowane są po 5–7 dniach.",
    "preparation": "Konsultacja kwalifikacyjna z chirurgiem: ocena stanu skóry, omówienie oczekiwanych efektów i wykluczenie przeciwwskazań.",
    "followup": "Zdjęcie szwów po 5–7 dniach. Powrót do codziennej aktywności zazwyczaj po 7–10 dniach."
  },
  "provider": { "@id": "https://medicare-radom.pl/#clinic" }
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Czy po zabiegu zostają blizny?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cięcia prowadzone są w naturalnym załamaniu powieki. Po wygojeniu ślady są niemal niedostrzegalne — nawet z bliska."
      }
    },
    {
      "@type": "Question",
      "name": "Jak długo utrzymuje się efekt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Efekt utrzymuje się zazwyczaj od 10 do nawet 15 lat. To jeden z najtrwalszych zabiegów odmładzających w medycynie estetycznej."
      }
    },
    {
      "@type": "Question",
      "name": "Ile wolnego muszę wziąć w pracy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Większość pacjentów wraca do aktywności już po 7–10 dniach. Szwy zdejmujemy po 5–7 dniach."
      }
    },
    {
      "@type": "Question",
      "name": "Czy zabieg jest bolesny?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nie. Wykonujemy go w znieczuleniu miejscowym — czujesz jedynie delikatne ukłucie przy wkłuciu. Reszta procedury jest komfortowa."
      }
    },
    {
      "@type": "Question",
      "name": "Ile kosztuje blefaroplastyka?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Plastyka powiek górnych: 3600 zł, dolnych: 4000 zł. Konsultacja kwalifikacyjna: 200 zł. Szczegóły w zakładce Usługi i cennik."
      }
    }
  ]
}
</script>
```

---

## poradnia-leczenia-ran.html

3 blocks.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "@id": "https://medicare-radom.pl/#clinic",
  "name": "Przychodnia MediCare",
  "description": "Wielospecjalistyczna przychodnia w Radomiu. Kardiolog, chirurg, neurolog, USG, RTG i Holter EKG.",
  "url": "https://medicare-radom.pl/",
  "logo": "https://medicare-radom.pl/assets/logo.png",
  "image": "https://medicare-radom.pl/assets/building.jpg",
  "telephone": "+48889834936",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "ul. Dębowa 2",
    "addressLocality": "Radom",
    "postalCode": "26-610",
    "addressCountry": "PL"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 51.3970839,
    "longitude": 21.1353775
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "08:00",
    "closes": "18:00"
  }],
  "sameAs": [
    "https://www.facebook.com/profile.php?id=61579875898421",
    "https://www.instagram.com/przychodnia_medicare/",
    "https://www.znanylekarz.pl/placowki/przychodnia-medicare-3"
  ],
  "medicalSpecialty": [
    "Cardiovascular",
    "Otolaryngologic",
    "Urologic",
    "Renal",
    "Neurologic",
    "Rheumatologic",
    "Psychiatric",
    "Surgical",
    "PlasticSurgery",
    "Radiography"
  ],
  "availableService": [
    { "@type": "MedicalTest", "name": "USG" },
    { "@type": "MedicalTest", "name": "RTG" },
    { "@type": "MedicalTest", "name": "Holter EKG" }
  ],
  "isAcceptingNewPatients": true,
  "hasMap": "https://maps.google.com/?q=ul.+D%C4%99bowa+2,+26-610+Radom"
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Strona główna", "item": "https://medicare-radom.pl/" },
    { "@type": "ListItem", "position": 2, "name": "Poradnie", "item": "https://medicare-radom.pl/poradnie.html" },
    { "@type": "ListItem", "position": 3, "name": "Poradnia Leczenia Ran", "item": "https://medicare-radom.pl/poradnia-leczenia-ran.html" }
  ]
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalWebPage",
  "name": "Poradnia Leczenia Ran – Radom",
  "url": "https://medicare-radom.pl/poradnia-leczenia-ran.html",
  "inLanguage": "pl-PL",
  "description": "Leczenie ran przewlekłych w Radomiu: terapia podciśnieniowa NPWT, larwoterapia, fibryna bogatopłytkowa PRF, zimna plazma, kompresjoterapia i specjalistyczne opatrunki.",
  "about": {
    "@type": "MedicalTherapy",
    "name": "Leczenie ran przewlekłych"
  },
  "mentions": [
    { "@type": "MedicalTherapy", "name": "Terapia podciśnieniowa (NPWT)" },
    { "@type": "MedicalTherapy", "name": "Larwoterapia" },
    { "@type": "MedicalTherapy", "name": "Fibryna bogatopłytkowa (PRF)" },
    { "@type": "MedicalTherapy", "name": "Zimna plazma" },
    { "@type": "MedicalTherapy", "name": "Kompresjoterapia" },
    { "@type": "MedicalCondition", "name": "Stopa cukrzycowa" },
    { "@type": "MedicalCondition", "name": "Owrzodzenia żylne i tętnicze podudzi" },
    { "@type": "MedicalCondition", "name": "Odleżyny" },
    { "@type": "MedicalCondition", "name": "Rany pooperacyjne i pourazowe z powikłanym gojeniem" },
    { "@type": "MedicalCondition", "name": "Oparzenia i owrzodzenia troficzne" }
  ],
  "provider": { "@id": "https://medicare-radom.pl/#clinic" }
}
</script>
```

---

## kontakt.html

3 blocks.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "@id": "https://medicare-radom.pl/#clinic",
  "name": "Przychodnia MediCare",
  "description": "Wielospecjalistyczna przychodnia w Radomiu. Kardiolog, chirurg, neurolog, USG, RTG i Holter EKG.",
  "url": "https://medicare-radom.pl/",
  "logo": "https://medicare-radom.pl/assets/logo.png",
  "image": "https://medicare-radom.pl/assets/building.jpg",
  "telephone": "+48889834936",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "ul. Dębowa 2",
    "addressLocality": "Radom",
    "postalCode": "26-610",
    "addressCountry": "PL"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 51.3970839,
    "longitude": 21.1353775
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "08:00",
    "closes": "18:00"
  }],
  "sameAs": [
    "https://www.facebook.com/profile.php?id=61579875898421",
    "https://www.instagram.com/przychodnia_medicare/",
    "https://www.znanylekarz.pl/placowki/przychodnia-medicare-3"
  ],
  "medicalSpecialty": [
    "Cardiovascular",
    "Otolaryngologic",
    "Urologic",
    "Renal",
    "Neurologic",
    "Rheumatologic",
    "Psychiatric",
    "Surgical",
    "PlasticSurgery",
    "Radiography"
  ],
  "availableService": [
    { "@type": "MedicalTest", "name": "USG" },
    { "@type": "MedicalTest", "name": "RTG" },
    { "@type": "MedicalTest", "name": "Holter EKG" }
  ],
  "isAcceptingNewPatients": true,
  "hasMap": "https://maps.google.com/?q=ul.+D%C4%99bowa+2,+26-610+Radom"
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Strona główna", "item": "https://medicare-radom.pl/" },
    { "@type": "ListItem", "position": 2, "name": "Kontakt", "item": "https://medicare-radom.pl/kontakt.html" }
  ]
}
</script>
```

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "name": "Kontakt – Przychodnia MediCare Radom",
  "url": "https://medicare-radom.pl/kontakt.html",
  "inLanguage": "pl-PL",
  "mainEntity": { "@id": "https://medicare-radom.pl/#clinic" }
}
</script>
```

---

## Validation

1. https://validator.schema.org/ — syntax and structure
2. https://search.google.com/test/rich-results — what Google can actually display

## Deliberately omitted

- `Review` and `AggregateRating` — Google does not display star ratings for
  self-published reviews. Ratings belong in Google Business Profile.
- `Product` — medical services are not products. Prices are expressed
  through `OfferCatalog` on the clinic entity instead.
- `VideoObject`, `Article` — no such content on the site.
