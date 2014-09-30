# 
# Copyright 2014 Google Inc. All rights reserved.
# 
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
# 

"""Tests for the geocoding module."""

import unittest
import datetime
import responses

import googlemaps

class GeocodingTest(unittest.TestCase):

    def setUp(self):
        self.key = 'AIzaasdf'
        self.ctx = googlemaps.Context(self.key)

    @responses.activate
    def test_simple_geocode(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.geocode(self.ctx, 'Sydney')

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'key=%s&address=Sydney' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_reverse_geocode(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.reverse_geocode(self.ctx, (-33.8674869, 151.2069902))

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'latlng=-33.867487%%2C151.206990&key=%s' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_geocoding_the_googleplex(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.geocode(self.ctx, '1600 Amphitheatre Parkway, '
                                  'Mountain View, CA')

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'key=%s&address=1600+Amphitheatre+Parkway%%2C+Mountain'
                          '+View%%2C+CA' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_geocode_with_bounds(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.geocode(self.ctx, 'Winnetka',
                                  bounds={'southwest': (34.172684, -118.604794),
                                          'northeast':(34.236144, -118.500938)})

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'bounds=34.172684%%2C-118.604794%%7C34.236144%%2C'
                          '-118.500938&key=%s&address=Winnetka' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_geocode_with_region_biasing(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.geocode(self.ctx, 'Toledo', region='es')

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'region=es&key=%s&address=Toledo' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_geocode_with_component_filter(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.geocode(self.ctx, 'santa cruz', 
            components={'country': 'ES'})

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'key=%s&components=country%%3AES&address=santa+cruz' % 
                          self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_geocode_with_multiple_component_filters(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.geocode(self.ctx, 'Torun', 
            components={'administrative_area': 'TX','country': 'US'})

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'key=%s&components=administrative_area%%3ATX%%7C'
                          'country%%3AUS&address=Torun' % self.key,
                          responses.calls[0].request.url)


    @responses.activate
    def test_geocode_with_just_components(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.geocode(self.ctx, 
            components={'route': 'Annegatan',
                        'administrative_area': 'Helsinki', 
                        'country': 'Findland'})

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'key=%s&components=administrative_area%%3AHelsinki'
                          '%%7Croute%%3AAnnegatan%%7Ccountry%%3AFindland' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_simple_reverse_geocode(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.reverse_geocode(self.ctx, (40.714224, -73.961452))

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'latlng=40.714224%%2C-73.961452&key=%s' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_reverse_geocode_restricted_by_type(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.reverse_geocode(self.ctx, (40.714224, -73.961452),
                                          location_type='ROOFTOP',
                                          result_type='street_address')

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'latlng=40.714224%%2C-73.961452&result_type=street_address&'
                          'key=%s&location_type=ROOFTOP' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_reverse_geocode_multiple_location_types(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.reverse_geocode(self.ctx, (40.714224, -73.961452),
                                          location_type=['ROOFTOP',
                                                         'RANGE_INTERPOLATED'],
                                          result_type='street_address')

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'latlng=40.714224%%2C-73.961452&result_type=street_address&'
                          'key=%s&location_type=ROOFTOP%%7CRANGE_INTERPOLATED' % 
                          self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_reverse_geocode_multiple_result_types(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.reverse_geocode(self.ctx, (40.714224, -73.961452),
                                          location_type='ROOFTOP',
                                          result_type=['street_address',
                                                       'route'])

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'latlng=40.714224%%2C-73.961452&result_type=street_address'
                          '%%7Croute&key=%s&location_type=ROOFTOP' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_partial_match(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.geocode(self.ctx, 'Pirrama Pyrmont')

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'key=%s&address=Pirrama+Pyrmont' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_utf_results(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/geocode/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.geocode(self.ctx, components={'postal_code': '96766'})

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/geocode/json?'
                          'key=%s&components=postal_code%%3A96766' % self.key,
                          responses.calls[0].request.url)
