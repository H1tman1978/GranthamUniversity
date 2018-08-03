# author: Adrian Rosebrock
# date: 27 January 2014
# website: http://www.pyimagesearch.com

# import the necessary packages
import numpy as np


def chi2_distance(hist_a, hist_b, eps=1e-10):
    # compute the chi-squared distance
    d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
                      for (a, b) in zip(hist_a, hist_b)])

    # return the chi-squared distance
    return d


class Searcher:
    def __init__(self, index):
        # store our index of images
        self.index = index

    def search(self, query_features):
        # initialize our dictionary of results
        results = {}

        # loop over the index
        for (k, features) in self.index.items():
            # compute the chi-squared distance between the features
            # in our index and our query features -- using the
            # chi-squared distance which is normally used in the
            # computer vision field to compare histograms
            d = chi2_distance(features, query_features)

            # now that we have the distance between the two feature
            # vectors, we can udpate the results dictionary -- the
            # key is the current image ID in the index and the
            # value is the distance we just computed, representing
            # how 'similar' the image in the index is to our query
            results[k] = d

        # sort our results, so that the smaller distances (i.e. the
        # more relevant images are at the front of the list)
        results = sorted([(v, k) for (k, v) in results.items()])

        # return our results
        return results
