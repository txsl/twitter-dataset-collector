// package txl11;

import eu.socialsensor.twcollect.TweetCorpusDownloader;


public class run {
public static void main(String args[])
    {
        System.out.println("Hello World");
        try{
            TweetCorpusDownloader.downloadIdsMultiThread("tweet_ids_only.txt_aa", "out.txt", true, 10);
        //     // downloadIdsMultiThread("tweet_ids_only.txt_aa", "out.txt", true, 10);
        }
        catch (Exception e){
            // return;
            System.out.println(e.getMessage());
        }
        // adIdsMultiThread("tweet_ids_only.txt_aa", "out.txt", true, 10);
        System.out.println("Hello World2");
    }
}