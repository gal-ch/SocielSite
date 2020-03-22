from allauth.socialaccount.templatetags.socialaccount import provider_login_url, ProviderLoginURLNode
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView
from .forms import BabysitterProfileForm, RecommendationsParentForm, \
    RecommendationsSitterForm, CreateSitterProfileForm, CreateParentProfileForm, ParentProfileForm
from .models import *


class LoginRequireMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequireMixin, self).dispatch(request, *args, **kwargs)


class BabysitterProfileListView(LoginRequiredMixin, ListView):
    login_url = ''
    redirect_field_name = 'sitter_list.html'
    template_name = 'profiles/babysitterprofile_list.html'
    queryset = BabysitterProfile.objects.prefetch_related('user__socialaccount_set')


class BabysitterProfileDetailView(LoginRequiredMixin, DetailView):
    model = BabysitterProfile

    def get_context_data(self, **kwargs):
        context = super(BabysitterProfileDetailView, self).get_context_data(**kwargs)
        context['recommendations_list'] = RecommendationsOfSitter.objects.filter(sitter=self.object)
        context['form'] = RecommendationsSitterForm()
        return context

    def post(self, request, pk):
        self.object = self.get_object()
        form = RecommendationsSitterForm(request.POST)
        if not form.is_valid():
            return self.get(request, pk)
        form.instance.author = request.user
        form.instance.sitter = self.object
        form.save()
        return redirect(request.path)

    # def friendlist(request):
    #     user = request.user
    #     # if user == sitter:
    #     userData = SocialToken.objects.get(account__user=request.user, account__provider='facebook')
    #     social = request.user.socialaccount_set.first().extra_data
    #     url = u'https://graph.facebook.com/{0}/' \
    #           u'friends?fields=id,name,location,picture' \
    #           u'&access_token={1}'.format(social['id'], userData, )
    #     re = urllib.request.urlopen(url)
    #     friends = json.loads(re.read()).get('data')
    #     if BabysitterProfile.objects.filter(user_id=user.pk).exists():
    #         userFriend = UserFriends.objects.filter(user_id=user.pk)
    #
    #     for friend in friends:
    #         userFriend.id = friend.get('id')
    #         userFriend.name = friend.get('name')
    #         userFriend.img = friend.get('picture')
    #         # userFriend.link
    #         userFriend.save()


class RecommendationsFormView(CreateView):
    form_class = RecommendationsSitterForm


class BabysitterProfileUpdate(UpdateView):
    model = BabysitterProfile
    form_class = BabysitterProfileForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user == obj.user:
            return super(BabysitterProfileUpdate, self).dispatch(request, *args, **kwargs)
        return redirect(reverse('core:sitter-list'))

    def get_initial(self):
        return {
            'email': self.get_object().user.email
        }

    def form_valid(self, form):
        data = form.cleaned_data
        email = data['email']
        # user = self.request.user
        self.email = email
        # user.save()
        return super().form_valid(form)


class BabysitterProfileCreate(CreateView):
    template_name = 'profiles/babysitterprofile_form.html'
    model = BabysitterProfile
    success_url = 'core:sitter-list'
    fields = ['city', 'age', 'about', 'experienceYears']

    # def get_initial(self):
    #     return {
    #         'email': self.request.user.email
    #     }

    def form_valid(self, form):
        form.instance.user = self.request.user
        o = form.save()
        return redirect(reverse('core:sitter-detail', args=[o.id]))


class ParentProfileListView(ListView):
    template_name = 'profiles/parerntprofile_list.html'
    queryset = ParentProfile.objects.prefetch_related('user__socialaccount_set')
    print(provider_login_url)


class ParentProfileDetailView(DetailView):
    model = ParentProfile

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ParentProfileDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['recommendations_list'] = RecommendationsOfParent.objects.filter(sitter=self.object)
        context['form'] = RecommendationsParentForm()
        return context

    def post(self, request, pk):
        print(request.user.pk)
        self.object = self.get_object()
        form = RecommendationsParentForm(request.POST)
        if not form.is_valid():
            return self.get(request, pk)
        form.instance.author = request.user
        form.instance.parent = self.object
        form.save()
        return redirect(request.path)


class ParentUpdate(UpdateView):
    model = ParentProfile
    form_class = ParentProfileForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user == obj.user:
            return super(ParentUpdate, self).dispatch(request, *args, **kwargs)
        return redirect(reverse('core:sitter-list'))

    def get_initial(self):
        return {
            'email': self.get_object().user.email
        }

    def form_valid(self, form):
        data = form.cleaned_data
        email = data['email']
        user = self.request.user
        user.email = email
        user.save()
        return super().form_valid(form)


# class CalendarView(generic.ListView):
#     model = Event
#     template_name = 'core/calendar.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # use today's date for the calendar
#         d = get_date(self.request.GET.get('day', None))
#         # Instantiate our calendar class with today's year and date
#         cal = Calendar(d.year, d.month)
#         # Call the formatmonth method, which returns our calendar as a table
#         html_cal = cal.formatmonth(withyear=True)
#         d = get_date(self.request.GET.get('month', None))
#         context['prev_month'] = prev_month(d)
#         context['next_month'] = next_month(d)
#         context['calendar'] = mark_safe(html_cal)
#         return context
#
#
# def get_date(req_day):
#     if req_day:
#         year, month = (int(x) for x in req_day.split('-'))
#         return date(year, month, day=1)
#     return datetime.today()
#
#
# def prev_month(d):
#     first = d.replace(day=1)
#     prev_month = first - timedelta(days=1)
#     month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
#     return month
#
#
# def next_month(d):
#     days_in_month = calendar.monthrange(d.year, d.month)[1]
#     last = d.replace(day=days_in_month)
#     next_month = last + timedelta(days=1)
#     print(next_month)
#     month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
#     return month
#
#
# def event(request, event_id=None):
#     instance = Event()
#     if event_id:
#         instance = get_object_or_404(Event, pk=event_id)
#     else:
#         instance = Event()
#
#     form = EventForm(request.POST or None, instance=instance)
#     if request.POST and form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse('core:calendar'))
#     return render(request, 'core/event.html', {'form': form})
#


