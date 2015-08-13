'''
Description: Prototype for scraping Apple App Store on iTunes and Google Play Apps reviews/Ratings
  
Created on 13 Aug 2015

@author: asilva
'''
def main():
    #
    print "Starting..."    
    # Import libraries
    import urllib
    import json
    import pprint
    
    def print_vars (var) :
        pprint.pprint(locals()) 
                        
    # Define URLs
    itunes_rating_url = "https://itunes.apple.com/lookup?id=400274934"
    itunes_review_url = "http://itunes.apple.com/rss/customerreviews/id=400274934/json"
    
    # Handle iTunes Rating
    json_rating_url = urllib.urlopen(itunes_rating_url);
    json_rating_res = json.load(json_rating_url)
    
    # Handle iTunes Reviews
    json_review_url = urllib.urlopen(itunes_review_url);
    json_review_res = json.load(json_review_url)
    
    print json_review_res
    
    for entry in json_review_res['feed']['entry']:
        #print json.dumps(entry , sort_keys=False, indent=4)
        print " ----------------------------------- "
        for (info, content) in entry.items():
            #print_vars(content)
            if info == 'im:rating':
                if isinstance(content, dict):
                    print " - %s : %s" % (info, content)
                    rating = content.get('label')
                    print rating
    
    
    
    
    ### Google Play HTML
    # Get if from here: http://www.crummy.com/software/BeautifulSoup/
    from bs4 import BeautifulSoup 
    
    html = '''
    <div class="review-text"> 
        <span class="review-title">??</span> I had to redo the same thing twice. When I signed out and logged back in they weren't even doing anything. Can't progress in the game if that keeps happening. 
        <div class="paragraph-end details-light"></div> 
    </div>
    <div class="featured-review-star-rating"> 
        <div aria-label=" Rated 1 stars out of five stars " class="tiny-star star-rating-non-editable-container"> 
            <div class="current-rating" style="width: 20%;">
            </div> 
        </div>
    </div>
    '''
    dom = BeautifulSoup(''.join(html), "html.parser")
    review = dom.find("div", {"class":"review-text"})
    print "Review Title: %s" % review.contents[1].contents[0]
    print "Review Content: %s" % review.contents[2]
    
#
if __name__== "__main__":
    main()    
