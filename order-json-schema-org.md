# Order

A Schema.org Type

[Thing](https://schema.org/Thing "Thing") > [Intangible](https://schema.org/Intangible "Intangible") > [Order](https://schema.org/Order "Order")

- Canonical URL: https://schema.org/Order
- [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Order)

An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.

| Property | Expected Type | Description |
| --- | --- | --- |
| Properties from [Order](https://schema.org/Order "Order") |     |     |
| `[acceptedOffer](https://schema.org/acceptedOffer "acceptedOffer")` | [Offer](https://schema.org/Offer "Offer") | The offer(s) – e.g., product, quantity and price combinations – included in the order. |
| `[billingAddress](https://schema.org/billingAddress "billingAddress")` | [PostalAddress](https://schema.org/PostalAddress "PostalAddress") | The billing address for the order. |
| `[broker](https://schema.org/broker "broker")` | [Organization](https://schema.org/Organization "Organization") or  <br>[Person](https://schema.org/Person "Person") | An entity that arranges for an exchange between a buyer and a seller. In most cases a broker never acquires or releases ownership of a product or service involved in an exchange. If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred. Supersedes [bookingAgent](https://schema.org/bookingAgent "bookingAgent"). |
| `[confirmationNumber](https://schema.org/confirmationNumber "confirmationNumber")` | [Text](https://schema.org/Text "Text") | A number that confirms the given order or payment has been received. |
| `[customer](https://schema.org/customer "customer")` | [Organization](https://schema.org/Organization "Organization") or  <br>[Person](https://schema.org/Person "Person") | Party placing the order or paying the invoice. |
| `[discount](https://schema.org/discount "discount")` | [Number](https://schema.org/Number "Number") or  <br>[Text](https://schema.org/Text "Text") | Any discount applied (to an Order). |
| `[discountCode](https://schema.org/discountCode "discountCode")` | [Text](https://schema.org/Text "Text") | Code used to redeem a discount. |
| `[discountCurrency](https://schema.org/discountCurrency "discountCurrency")` | [Text](https://schema.org/Text "Text") | The currency of the discount.  <br><br/>Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. “USD”; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. “BTC”; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. “Ithaca HOUR”. |
| `[isGift](https://schema.org/isGift "isGift")` | [Boolean](https://schema.org/Boolean "Boolean") | Indicates whether the offer was accepted as a gift for someone other than the buyer. |
| `[orderDate](https://schema.org/orderDate "orderDate")` | [Date](https://schema.org/Date "Date") or  <br>[DateTime](https://schema.org/DateTime "DateTime") | Date order was placed. |
| `[orderDelivery](https://schema.org/orderDelivery "orderDelivery")` | [ParcelDelivery](https://schema.org/ParcelDelivery "ParcelDelivery") | The delivery of the parcel related to this order or order item. |
| `[orderNumber](https://schema.org/orderNumber "orderNumber")` | [Text](https://schema.org/Text "Text") | The identifier of the transaction. |
| `[orderStatus](https://schema.org/orderStatus "orderStatus")` | [OrderStatus](https://schema.org/OrderStatus "OrderStatus") | The current status of the order. |
| `[orderedItem](https://schema.org/orderedItem "orderedItem")` | [OrderItem](https://schema.org/OrderItem "OrderItem") or  <br>[Product](https://schema.org/Product "Product") or  <br>[Service](https://schema.org/Service "Service") | The item ordered. |
| `[partOfInvoice](https://schema.org/partOfInvoice "partOfInvoice")` | [Invoice](https://schema.org/Invoice "Invoice") | The order is being paid as part of the referenced Invoice. |
| `[paymentDueDate](https://schema.org/paymentDueDate "paymentDueDate")` | [Date](https://schema.org/Date "Date") or  <br>[DateTime](https://schema.org/DateTime "DateTime") | The date that payment is due. Supersedes [paymentDue](https://schema.org/paymentDue "paymentDue"). |
| `[paymentMethod](https://schema.org/paymentMethod "paymentMethod")` | [PaymentMethod](https://schema.org/PaymentMethod "PaymentMethod") or  <br>[Text](https://schema.org/Text "Text") | The name of the credit card or other method of payment for the order. |
| `[paymentMethodId](https://schema.org/paymentMethodId "paymentMethodId")` | [Text](https://schema.org/Text "Text") | An identifier for the method of payment used (e.g. the last 4 digits of the credit card). |
| `[paymentUrl](https://schema.org/paymentUrl "paymentUrl")` | [URL](https://schema.org/URL "URL") | The URL for sending a payment. |
| `[seller](https://schema.org/seller "seller")` | [Organization](https://schema.org/Organization "Organization") or  <br>[Person](https://schema.org/Person "Person") | An entity which offers (sells / leases / lends / loans) the services / goods. A seller may also be a provider. Supersedes [merchant](https://schema.org/merchant "merchant"), [vendor](https://schema.org/vendor "vendor"). |
| Properties from [Thing](https://schema.org/Thing "Thing") |     |     |
| `[additionalType](https://schema.org/additionalType "additionalType")` | [Text](https://schema.org/Text "Text") or  <br>[URL](https://schema.org/URL "URL") | An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. Typically the value is a URI-identified RDF class, and in this case corresponds to the use of rdf:type in RDF. Text values can be used sparingly, for cases where useful information can be added without their being an appropriate schema to reference. In the case of text values, the class label should follow the schema.org [style guide](https://schema.org/docs/styleguide.html). |
| `[alternateName](https://schema.org/alternateName "alternateName")` | [Text](https://schema.org/Text "Text") | An alias for the item. |
| `[description](https://schema.org/description "description")` | [Text](https://schema.org/Text "Text") or  <br>[TextObject](https://schema.org/TextObject "TextObject") | A description of the item. |
| `[disambiguatingDescription](https://schema.org/disambiguatingDescription "disambiguatingDescription")` | [Text](https://schema.org/Text "Text") | A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation. |
| `[identifier](https://schema.org/identifier "identifier")` | [PropertyValue](https://schema.org/PropertyValue "PropertyValue") or  <br>[Text](https://schema.org/Text "Text") or  <br>[URL](https://schema.org/URL "URL") | The identifier property represents any kind of identifier for any kind of [Thing](https://schema.org/Thing), such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](https://schema.org/docs/datamodel.html#identifierBg) for more details. |
| `[image](https://schema.org/image "image")` | [ImageObject](https://schema.org/ImageObject "ImageObject") or  <br>[URL](https://schema.org/URL "URL") | An image of the item. This can be a [URL](https://schema.org/URL) or a fully described [ImageObject](https://schema.org/ImageObject). |
| `[mainEntityOfPage](https://schema.org/mainEntityOfPage "mainEntityOfPage")` | [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or  <br>[URL](https://schema.org/URL "URL") | Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](https://schema.org/docs/datamodel.html#mainEntityBackground) for details.  <br>Inverse property: [mainEntity](https://schema.org/mainEntity "mainEntity") |
| `[name](https://schema.org/name "name")` | [Text](https://schema.org/Text "Text") | The name of the item. |
| `[potentialAction](https://schema.org/potentialAction "potentialAction")` | [Action](https://schema.org/Action "Action") | Indicates a potential Action, which describes an idealized action in which this thing would play an ‘object’ role. |
| `[sameAs](https://schema.org/sameAs "sameAs")` | [URL](https://schema.org/URL "URL") | URL of a reference Web page that unambiguously indicates the item’s identity. E.g. the URL of the item’s Wikipedia page, Wikidata entry, or official website. |
| `[subjectOf](https://schema.org/subjectOf "subjectOf")` | [CreativeWork](https://schema.org/CreativeWork "CreativeWork") or  <br>[Event](https://schema.org/Event "Event") | A CreativeWork or Event about this Thing.  <br>Inverse property: [about](https://schema.org/about "about") |
| `[url](https://schema.org/url "url")` | [URL](https://schema.org/URL "URL") | URL of the item. |

Instances of [Order](https://schema.org/Order "Order") may appear as a value for the following properties

| Property | On Types | Description |
| --- | --- | --- |
| [partOfOrder](https://schema.org/partOfOrder "partOfOrder") | [ParcelDelivery](https://schema.org/ParcelDelivery "ParcelDelivery") | The overall order the items in this delivery were included in. |
| [referencesOrder](https://schema.org/referencesOrder "referencesOrder") | [Invoice](https://schema.org/Invoice "Invoice") | The Order(s) related to this Invoice. One or more Orders may be combined into a single Invoice. |

### Examples

[Example 1](https://schema.org/Order#eg-0375 "Link: #eg-0375")

No Markup Microdata RDFa JSON-LD Structure

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

    <script type="application/ld+json">
    {
        "@context": "https://schema.org/",
        "@type": "Invoice",
        "broker": {
          "@type": "LocalBusiness",
          "name": "ACME Home Heating"
        },
        "accountId": "xxxx-xxxx-xxxx-1234",
        "customer": {
          "@type": "Person",
          "name": "Jane Doe"
        },
        "paymentDueDate": "2015-01-30",
        "minimumPaymentDue": {
          "@type": "PriceSpecification",
          "price": 0.00,
          "priceCurrency": "USD"
        },
        "totalPaymentDue": {
          "@type": "PriceSpecification",
          "price": 0.00,
          "priceCurrency": "USD"
        },
        "paymentStatus": "https://schema.org/PaymentComplete",
        "referencesOrder": [
          {
            "@type": "Order",
            "description": "furnace",
            "orderDate": "2014-12-01",
            "orderNumber": "123ABC",
            "paymentMethod": "http://purl.org/goodrelations/v1#ByInvoice",
            "orderedItem": {
              "@type": "Product",
              "name": "ACME Furnace 3000",
              "productID": "ABC123"
            }
          },
          {
            "@type": "Order",
            "description": "furnace installation",
            "orderDate": "2014-12-02",
            "paymentMethod": "http://purl.org/goodrelations/v1#ByInvoice",
            "orderedItem": {
              "@type": "Service",
              "description": "furnace installation"
            }
          }
        ]
    }
    </script>

[Example 2](https://schema.org/Order#eg-0376 "Link: #eg-0376")

No Markup Microdata RDFa JSON-LD Structure

Example encoded as [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) in a HTML script tag.

    <script type="application/ld+json">
    {
      "@context": "https://schema.org/",
      "@type": "Order",
      "seller": {
        "@type": "Organization",
        "name": "ACME Supplies"
      },
      "customer": {
        "@type": "Person",
        "name": "Jane Doe"
      },
      "orderedItem": [
        {
          "@type": "OrderItem",
          "orderItemNumber": "abc123",
          "orderQuantity": 1,
          "orderedItem": {
            "@type": "Product",
            "name": "Widget"
          },
          "orderItemStatus": "https://schema.org/OrderDelivered",
          "orderDelivery": {
            "@type": "ParcelDelivery",
            "expectedArrivalFrom": "2015-03-10"
          }
        },
        {
          "@type": "OrderItem",
          "orderItemNumber": "def456",
          "orderQuantity": 3,
          "orderedItem": {
            "@type": "Product",
            "name": "Widget accessories"
          },
          "orderItemStatus": "https://schema.org/OrderInTransit",
          "orderDelivery": {
            "@type": "ParcelDelivery",
            "expectedArrivalFrom": "2015-03-15",
            "expectedArrivalUntil": "2015-03-18"
          }
        }
      ]
    }
    </script>

