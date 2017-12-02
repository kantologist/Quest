def bid_statistics(id):
    auction = Auction.query.filter_by(id=id).first()
    bids = auction.bids.all()
    bid_prices = [bid.price for bid in bids]
    avg = sum(bid_prices)/len(bid_prices)
    mode = max(set(bid_prices), key=bid_prices.count)
    half = len(bid_prices) // 2
    bid_prices.sort()
    if not len(bid_prices) % 2:
        median = (bid_prices[half - 1] + bid_prices[half]) / 2.0
    else:
        median = bid_prices[half]
    return {"mean": avg,
            "median": median,
            "mode": mode,
            "min": min(bid_prices),
            "max":max(bid_prices)}
