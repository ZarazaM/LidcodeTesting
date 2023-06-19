# TODO заполнить
from models.sponsors import DefaultSponsor, SponsorDict, UpdateSponsor
from utils.assertions.base.expect import expect


def assert_sponsor(
        expected_sponsor: SponsorDict,
        actual_sponsor: DefaultSponsor | UpdateSponsor
):
    pass
#     if isinstance(actual_sponsor, DefaultSponsor):
#         expect(expected_sponsor['id']).set_description('Sponsor id').to_be_equal(actual_sponsor.id)
#
#     expect(expected_sponsor['link']).set_description('Sponsor link').to_be_equal(actual_sponsor.link)
#
#     expect(expected_sponsor['name']).set_description('Sponsor name').to_be_equal(actual_sponsor.name)
