import dns.resolver
karim=dns.resolver.query("google.com","A",raise_on_no_answer=False)
#"A" ======> ipv4 to FQDN
#"AAA" =====> ipv6 to FQDN
#"CNAME" ====> FQDN to FQDN
#"MX" ======> Pour spécifier les serveurs de messagerie pour un domaine spécifique
#"NS" ===> Spécifie les serveurs DNS responsables d'un domaine particulier
#"SOA" =====> Utilisé pour définir les informations administratives sur le domaine
#"PTR" =====> Utilisé pour associer une adresse IP à un nom de domaine
for value in karim :
    print ("host===>",value.to_text())