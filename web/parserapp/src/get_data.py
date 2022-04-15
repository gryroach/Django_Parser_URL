from requests import get
import logging
from django.conf import settings
from .parsers import ParserLinks
from ..models import DomainModel, MxModel
from ..serializers import DomainSerializer


def find_from_api(in_domain):
    open_api = settings.OPEN_API_DOMAIN
    payload = {'domain': in_domain}
    result = []

    try:
        response = get(open_api, params=payload)
        for domain in response.json()['domains']:
            if in_domain in domain['domain']:
                result.append(domain)
    except Exception as er:
        logging.warning(f"Error while trying to get domains: {er}")

    return result


def create_records_db(url):
    domains_model_objects = []
    mx_model_objects = []
    links = ParserLinks(url).find_links()

    for link in links:
        domain = ParserLinks(link).domain
        remote_data = find_from_api(domain)
        for data in remote_data:
            data['url'] = link
            serializer = DomainSerializer(data=data)
            if serializer.is_valid():
                mx_data = serializer.validated_data.pop("MX", None)
                domain_object = DomainModel(**serializer.validated_data)
                for i_mx in mx_data:
                    mx_model_objects.append(MxModel(domain=domain_object, **i_mx))
                domains_model_objects.append(domain_object)

    DomainModel.objects.bulk_create(domains_model_objects)
    MxModel.objects.bulk_create(mx_model_objects)

    return {"Count of found link": len(links), "Count of added domain": len(domains_model_objects)}
