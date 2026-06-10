# OpenSSL Reference Commands

Commands used during S/MIME certificate and PKCS#12 experimentation.

## View PKCS#12 Information

```bash
openssl pkcs12 -info -in cert.pfx -nodes
```

## View Certificates or Private Key Only

```bash
openssl pkcs12 -info -in cert.pfx -nodes -nocerts
openssl pkcs12 -info -in cert.pfx -nodes -nokeys
```

## Export Certificates and Private Keys to Files

```bash
openssl pkcs12 -info -in cert.pfx -out skey.pem -nodes -nocerts
openssl pkcs12 -info -in cert.pfx -out certificate.crt -nodes -nokeys
```

## Inspect Exported Material

```bash
openssl rsa -in skey.pem -text
openssl x509 -in certificate.crt -text
```

## Change PKCS#12 Password

```bash
openssl pkcs12 -in "PKCSFile" -nodes | openssl pkcs12 -export -out "PKCSFile-Nopass"
```
